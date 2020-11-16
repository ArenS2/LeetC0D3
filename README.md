# Problem

```sh
Oh no! I have accidentally blacklisted my admin credentials, can you help me to find a way to break in?
nc challs.ctf.m0lecon.it 8000
Author: @matpro
[CHALLENGE.PY]
```
# Solution

- Vì đây là bài writeup đầu tiên của mình về mảng **Crypto**  nên có thể sẽ  không đầy đủ như ý đồ của tác giả.  Tuy nhiên mình sẽ cố gắng viết chi tiết một tí.
- Đầu tiên khi vào bài này, tác giả cho chúng ta 1 file [challenge.py](problem/challenge.py)
- File code đó tương đối dài nên mình sẽ tóm tắt những ý quan trọng về nội dung của file code đó:
	- Đầu tiên tác giả tạo sẵn 1 biến nguyên `p` rất lớn (2049 bits) 
	```sh
	p = 43401284375631863165968499011197727448907264840342630537012422089599453290392542589198227993829403166459913232354777490444915201356560807401141203961578150815557853865678753463969663318864902106651761912058979552119867603661163587639785030788676120329044248495611269533429749805119341551183130515359738240737511058829539566547367223386189286492001611298474857947463007621758421914760578235374029873653721324392107800911728989887542225179963985432894355552676403863014228425990320221892545963512002645771206151750279770286101983884882943294435823971377082846859794746562204984002166172161020302386671098808858635655367
	```	
	- Sau đó tác giả tạo ra 2 biến số nguyên `x`, `y` ngẫu nhiên có độ dài 32 bytes (256 bits).
	```sh
	x = bytes_to_long(urandom(32))
	y = bytes_to_long(urandom(32))
	```
	- Tiếp theo tác giả tạo 2 biến số nguyên `a`, `b` có giá trị tương ứng `a = 418296719726` & `b = 8097880544751088228`
	```sh
	a = bytes_to_long(b'admin')
	b = bytes_to_long(b'password')
	```
	- Bây giờ tác giả đặt ra 1 biến `server_hash` có giá trị bằng (x<sup>a</sup> % p)\*(y<sup>b</sup> % p) % p. Ta có `a`, `b`, `p` cố định nhưng vì `x`, `y` thay đổi nên `server_hash` sẽ luôn thay đổi sau mỗi lần kết nối đến server.
	```sh
	server_hash = (pow(x, a, p) * pow(y, b, p)) % p
	```
	- Bài toán đặt ra ở đây sẽ là: chúng ta sẽ tìm và nhập 2 biến `username` & `password` (tạm thay bằng `m`, `n` tương ứng) sao cho: 
		- (x<sup>m</sup> % p)\*(y<sup>n</sup> % p) % p == `server_hash` 
	- Hay 1 cách dễ hiểu đề bài sẽ là: với `p`, `x`, `y`, `a`, `b` cho trước, tìm `m`, `n` (lần lượt khác `a`, `b`) sao cho: 
		- (x<sup>a</sup> % p)\*(y<sup>b</sup> % p) % p == (x<sup>m</sup> % p)\*(y<sup>n</sup> % p) % p
- Vì đây là lần đầu chơi **Crypto** ở những dạng thiên về toán học như thế này, việc đầu tiên của mình là ngơ ngác nhìn đề, đọc thuật toán và chẳng biết làm gì tiếp theo. Sau vài canh giờ ngu ngơ, mình bắt đầu xem youtube, photo tài liệu, học lại số học: số nguyên tố, đồng dư các kiểu. Cảm giác như vừa khóc vừa học lại các kiến thức từ hồi tận cấp 2 :haiz. Rồi sau gần chục tiếng loay hoay mà không có kết quả, còn vài giờ nữa là cuộc thi kết thúc, mình vô tình phát hiện ra bài toán này trong 1 slide nào đó của tụi học sinh cấp 2:
<img src=assets/a1.png>
- Không chần chờ gì nữa, mình nhảy vào test ngay và kết quả không ngoài mong đợi: 
<img src=assets/a2.png>

- Đến đây cảm giác gần giải ra càng ngày càng rõ ràng hơn, mình bắt đầu viết lại phương trình và yêu cầu đề cho:
	- (1): x<sup>a</sup> . y<sup>b</sup> ≡ k (mod p)
	- (2): x<sup>m</sup> . y<sup>n</sup> ≡ k (mod p)
- Chuyện sẽ chẳng đi đến đâu, bài toán cũng chẳng thể giải nếu chỉ 2 phương trình trên. Tuy nhiên, mấu chốt vấn đề chính là nằm ở số nguyên `p` cực lớn kia cùng với bài toán cấp 2 mình vừa phát hiện. Nhờ vào tụi nó mà mình có ngay phương trình thứ 3 - phương trình cứu rỗi bài toán :xD
	- (3): x<sup>p-1</sup> . y<sup>p-1</sup> ≡ 1 (mod p)
- Ngay sau đó áp dụng ngay các kiến thức cơ bản vừa được ôn lại:
<img src=assets/a3.png>
- Lấy (1) * (3) vế theo vế và so sánh với (2) ta được:
x<sup>a+p-1</sup> . y<sup>b+p-1</sup> ≡ x<sup>m</sup> . y<sup>n</sup> (mod p)
- Từ đó cho 2 chúng nó bằng nhau và ta tính được: `m = a + p - 1` và `n = b + p -1`
- Về mặt lý thuyết ta đã giải xong bài toán, nhưng trong code bài cho nó chặt chẽ hơn: chỉ cho phép độ dài của `m`, `n` ở hệ hex <= 512 kí tự, nhưng với kết quả ta vừa tính được, độ dài của cả `m` và `n` đều là 513
<img src=assets/a4.png>
```sh
try:
	print('Username:')
	username = input()
	assert len(username) <= 512
	username = unhexlify(username)
	print('Password:')
	password = input()
	assert len(password) <= 512
	password = unhexlify(password)
except:
	print("Input too long! I can't keep in memory such long data")
	exit()

if username == b'admin' or password == b'password':
	print("Intrusion detected! Admins can login only from inside our LAN!")
	exit()
``` 
- Do đó, từ 3 phương trình đó ta phải biến đổi lại 1 chút để giảm được giá trị `m` và `n`.
- Ta lấy (1)<sup>2</sup> \* (3) rồi so sánh với (2)<sup>2</sup>, ta được:
x<sup>2a+p-1</sup>.y<sup>2b+p-1</sup> ≡ x<sup>2m</sup>.y<sup>2n</sup> (mod p)
- Cho thẳng 2 chúng nó bằng nhau ta được `m = a + (p-1)/2` và `n = b + (p-1)/2`.
```sh
m = 21700642187815931582984249505598863724453632420171315268506211044799726645196271294599113996914701583229956616177388745222457600678280403700570601980789075407778926932839376731984831659432451053325880956029489776059933801830581793819892515394338060164522124247805634766714874902559670775591565257679869120368755529414769783273683611693094643246000805649237428973731503810879210957380289117687014936826860662196053900455864494943771112589981992716447177776338201931507114212995160110946272981756001322885603075875139885143050991942441471647217911985688541423429897373281102492001083086080510151193335549404847614547409
n = 21700642187815931582984249505598863724453632420171315268506211044799726645196271294599113996914701583229956616177388745222457600678280403700570601980789075407778926932839376731984831659432451053325880956029489776059933801830581793819892515394338060164522124247805634766714874902559670775591565257679869120368755529414769783273683611693094643246000805649237428973731503810879210957380289117687014936826860662196053900455864494943771112589981992716447177776338201931507114212995160110946272981756001322885603075875139885143050991942441471647217911985688541423429897373281102492001083086080510151193343647284974068915911
```
- Kiểm tra thì thỏa mãn với yêu cầu độ dài. Giờ chỉ việc chuyển sang hệ hex (theo yêu cầu trong code) và submit thôi:
<img src=assets/a5.png>

**P/s: Nói chung là vã thật nhưng mà vui :vv**
