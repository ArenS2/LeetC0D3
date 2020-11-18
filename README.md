# Problem
```sh
BreakMe
500
I encrypted important information and lost my private key!

Can you help me to recover the content of the file?
[encrypted.txt]   [public.pem]
```
# Solution
- Vì đây là 1 dạng toán về thuật toán mã hóa RSA nên mình có thể sẽ viết dài 1 tí vì mỗi lần nhắc đến thèn này mình lại sợ vcl ra, hôm nay có dịp gặp lại nên viết 1 bài tóm tắt luôn, khỏi mất công mỗi lần gặp lại đi search google, mà mình lại thường search ngu nữa nên ... :haiz

- Solution này gồm 3 phần:
	- Giới thiệu về RSA 
	- Giải cái `problem` bên trên
	- Bonus
## Giới thiệu về RSA
### Tóm tắt ngắn gọn:
- Khi nhắc đến thuật toán mã hóa `RSA` thì các bạn sẽ thường nghĩ ngay đến 2 thứ đó là `public_key` (khóa công khai) và `private_key` (khóa bí mật), ngoài ra tất nhiên sẽ còn có `plain_text` (thông điệp gốc) và `cipher_text` (thông điệp đã được mã hóa). 

- Vậy cách nó hoạt động ra sao? Đầu tiên bạn sẽ có 1 đoạn `plain_text` (thư tình chẳng hạn) muốn gởi đi, nhưng vì sợ người khác đọc được nên bạn có nhu cầu mã hóa cái `plain_text` đó. Muốn mã hóa thì cũng phải có thuật toán, giả sử bạn chọn RSA. Khi sử dụng RSA bạn sẽ có được 2 cái key: `public_key` & `private_key`. Nguyên lí hoạt động cũng đơn giản thôi: bạn sẽ dùng cái `public_key` đó để mã hóa cái `plain_text`, sau khi bị mã hóa thì cái `plain_text` đó sẽ trở thành `cipher_text` (ở dạng `cipher_text` thì bạn sẽ không đọc được bức thư đó đâu). Và đó là mã hóa, vậy muốn giải mã cái `cipher_text` đó thì làm sao? Đơn giản thôi, sử dụng cái key thứ 2 của RSA kìa - `private_key`.

- Vậy vấn đề ở đây sẽ là bên trong cái `public_key` và `private_key` có những gì mà có thể làm được như vậy? Câu trả lời sẽ là:
	- `public_key` gồm có: `e`, `n`.
	- `private_key` gồm có: `d`, `e`, `n` (thật ra mà nói theo mình kiểm tra thì thèn này có hết `n`, `e`, `d`, `p`, `q`. Nhưng theo kiến thức hiện tại của mình thì thèn `d` mới là quan trọng vì nó là thèn `giải mã`, còn mấy thèn còn lại chắc dùng để so khớp giữa `public_key` và `private_key` xem chúng nó có đúng là 1 cặp `key` hay không)

- Vậy đến đây ta biết được thật chất `public_key` hay `private_key` sẽ gồm `p`, `q`, `n`, `e`, `d`. Vậy những thèn này là gì? cách nó được tạo ra như thế nào? và cách nó mã hóa & giải mã ra sao? (chuẩn bị đến phần toán học :lol)

- Let's get started:
	- Đầu tiên, tạo ngẫu nhiên 2 số nguyên tố `p`, `q` khác nhau (`prime1`, `prime2`) (2 số này càng lớn thì thuật toán RSA càng an toàn)
	- Tiếp theo sẽ tính `n`: `n = p*q` (`n` còn được gọi là `Modulus`)
	- Tiếp theo sẽ tính `ϕ`: `ϕ = (p-1)*(q-1)` (`ϕ` được gọi là `Hàm Euler`)
	- Sau đó sẽ chọn `e`: `e < n` và `gcd(e, ϕ) = 1` (`gcd: Ước chung lớn nhất`, `e: publicExponent` )
	- Tới đây đã có `n` và `e` để tạo `public_key` rồi.
	- Đã có `e` để mã hóa thì phải có `d` để giải mã: chọn `d` sao cho `d*e ≡ 1 (mod ϕ)` (`d: privateExponent`)
	- Đến đây là đủ các thành phần để tạo `public_key` và `private_key` rồi đó.
	- Thêm 1 tí: nói luôn `plain_text` và `cipher_text` ha.
	- Gọi `m` là `plain_text`, `c` là `cipher_text`, khi đó ta sẽ có:
		- Lúc mã hóa: c = m<sup>e</sup> (mod n) (Lưu ý: 1 < m < n)
		- Khi giải mã: m = c<sup>d</sup> (mod n)
- Đấy cơ bản chỉ có vậy thôi. Tiếp theo demo phát cho nóng:

### Example:
- Đầu tiên, chọn 2 số nguyên tố ngẫu nhiên khác nhau: `p = 7` và `q = 13`

- Tiếp theo tính `Modulus n`: `n = p*q = 91`

- Tiếp theo tính `Hàm Euler ϕ`: `ϕ = (p-1)*(q-1) = 72`

- Sau đó chọn `e = 5` vì `gcd(e, ϕ) = gcd(5, 72) = 1`

- Tiếp theo chọn `d = 29` vì `d.e ≡ 1 (mod ϕ)`

- Giả sử ta có `plain_text` `m = 69`, theo công thức ở trên thì `c` = m<sup>e</sup> (mod n). Do đó `c = 62`.

- Bây giờ thử dùng `d` để giải mã `c` để xem thử có lấy lại được `m = 69` không nhé.

- `m` = c<sup>d</sup> (mod n). Và tính ra thì đúng là `m = 69` thật.

---> Đấy thế là bạn đã hiểu phần nào về RSA rồi đấy, bây giờ đã đủ tự tin để làm cái đề kia thôi :xD

## Solve Crypto problem
- Đề bài cho chúng ta 2 file: [encrypted](problem/encrypted.txt) và [public.pem](problem/public.pem)

- Vừa nhìn vào cái đuôi file `.pem` là nghĩ ngay đến RSA rồi. Bây giờ cùng nhìn xem file `public_key` bên trong nó sẽ như thế nào nhá :excited_icon
<img src=assets/p1.png>

- Đấy, đấy là định dạng của 1 file `public_key`. Cơ mà có thấy `n` và `e` đâu ta :xD. Ok, bây giờ chúng ta sẽ sử dụng tool `openssl` (tool này hơi bị đỉnh, nhiều chức năng lắm) để lấy được dữ liệu thật sự được chứa bên trong dưới vỏ bọc của định dạng file `.pem` nhá.
```sh
openssl rsa -pubin -in public.pem -text -noout
```
<img src=assets/p2.png>

- Khi đó ta sẽ có ngay 2 giá trị `n` (`Modulus`) và `e` (`Exponent` or `publicExponent`)
```sh
n = 0xbe5f670c7cdfcc0bd34112d3bd71229fd3e446e531bf3516036c1258336f6c51
e = 0x10001
```
- Vâng, lúc này chúng ta đã có `public_key`, ngoài ra còn cả cả `cipher_text`, chính là nội dung trong file [encrypted.txt](problem/encrypted.txt) kia. Cơ mà chỉ có `n`, `e`, và `c` thì làm sao chúng ta có thể giải mã mà không có `d` được. Do đó chúng ta phải đi tìm `d` từ `e` và `n` có sẵn kia.

- Để xem lúc nãy `d` được tính như nào: `d*e ≡ 1 (mod ϕ)`

- Chúng ta đã có `e` nhưng chưa có `ϕ` mà `ϕ = (p-1)*(q-1)`, mà chúng ta đã có `p`, `q` đâu cơ chứ.

- Quay lại lên trên xem lý thuyết tiếp ta thấy `n = p*q`. Cũng may bài này dễ nên tác giả chọn `p`, `q` nhỏ nên `n` cũng nhỏ theo. Giới thiệu luôn trên mạng có trang này [factordb.com](http://factordb.com/) dùng để phân tích 1 số ra tích của các số nguyên tố, cái hay ở trang này so với các trang khác là nó phân tích được những số lớn. OK, đem vào đó `Factorize` ta sẽ có ngay 2 số `p` và `q`.
```sh
n = 86108002918518428671680621078381724386896258624262971787023054651438740237393
p = 286748798713412687878508722355577911069
q = 300290718931931563784555212798489747397
```
- Sau khi có `p`, `q` thì `ϕ = (p-1)*(q-1)`
```sh
ϕ = 86108002918518428671680621078381724386309219106617627535359990716284672578928
```
- Tiếp tục đến cái này mới khoai: `d*e ≡ 1 (mod ϕ)`. Vì `ϕ` quá lớn nên những đoạn code chuối của mình đều không ăn thua. Tiếp tục search google thì thấy được thèn [này](https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python/9758173#9758173). Và dưới đây là đoạn code giúp chúng ta có thể tính ra được `d`.
```sh
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
```
- Sau khi đã có `d` rồi, việc còn lại là giải mã thôi. Nhưng trước tiên phải mở file [encrypted](problem/encrypted.txt) ra, lấy nội dung bên trong chuyển thành số nguyên rồi mới áp dụng công thức giải mã được: m = c<sup>d</sup> (mod n).
<img src=assets/p3.png>

- Và lúc này ta đã có:
```sh
n = 86108002918518428671680621078381724386896258624262971787023054651438740237393
c = 74806200070710430428438847316507311847202230565058608921850842031191743309425
d = 52563235496868154743721179285926106867856121268586368115409795819089744895137
```
- Áp dụng công thức giải mã: m = c<sup>d</sup> (mod n) ta tính ngay ra được `d = 3998731487633352107852441255033768239881091376738602013454220231226719498`. Việc còn lại là chuyển số này thành chuỗi kí tự là xong.
<img src=assets/p4.png>

- Cuối cùng `flag` sẽ là **AFFCTF{PermRecord}**. (Đoạn chuyển flag từ `int` sang `string` cẩn thận tí nhé :vv) 
- File code dành cho bài này mình để ở [đây](solve/solve.py).

## Bonus
- Còn bây giờ là phần ngoài bài toán 1 tí. Thật ra trước giờ lúc tạo 2 file `public_key` và `private_key` mình toàn dùng tools để tạo, à không tools thì phải dùng rồi vì cho mình code tools đó chắc cũng khóc dở, ý mình là khi dùng tools ấy thì mấy tham số `p`, `q`, `n`, `e`, `d` đều do tools tạo ngẫu nhiên hết. Với nhu cầu hiện tại của mình, mình muốn tạo 2 file `key` đó với các tham số do mình định sẵn nên mình mới viết cái `Bonus` này để lưu lại quá trình  (Sau này lỡ muốn tự tạo file `public_key` và `private_key` cho riêng mình thì cũng biết đường mà làm :hehe).

- OK, bắt đầu làm thôi, để làm và test độ đúng sai luôn thì mình lấy các tham số `n`, `e`, `d` giống như bài trên, chặp nữa lúc endgame ra được file `public_key` trùng với file `public_key` [public.pem](problem/public.pem) của đề cho là ok.
```sh
n = 86108002918518428671680621078381724386896258624262971787023054651438740237393
p = 286748798713412687878508722355577911069
q = 300290718931931563784555212798489747397
ϕ = 86108002918518428671680621078381724386309219106617627535359990716284672578928
e = 65537
d = 3998731487633352107852441255033768239881091376738602013454220231226719498
```
- Thế là đã xác định xong các giá trị ban đầu. Tiếp theo chúng ta cần tạo 1 file [config](solve/temp.conf) để lưu các giá trị này vào (+ thêm 1 số giá trị khác nữa (tuy nhiên đều được tính dựa trên các giá trị cốt lõi này))
	- `e1 = d mod(p-1)`
	- `e2 = d mod(q-1)`
	- `coeff = q^-1 mod(p)`. Thèn này khó hiểu 1 tí tí đúng không, thật ra nó sẽ là: `q*coeff ≡ 1 mod(p)`. Áp dụng công thức bên trên (lúc tìm `d` trong `e*d ≡ 1 mod(ϕ)`) cũng được. Ngoài cách này ra còn có cách khác, vì `p` là số nguyên tố nên: `coeff` = q<sup>p-2</sup> mod(p). Lúc đó ta sẽ tính được các giá trị này:
```sh
e1 = 79871076793700741133958703119866436054
e2 = 297452792678365151939346760860803354174
coeff = 43340310015875206124799642386915239847
```
- Khi đó chúng ta sẽ được file [config.conf](solve/config) như thế này:
```sh
asn1=SEQUENCE:rsa_key

[rsa_key]
version=INTEGER:0
modulus=INTEGER:86108002918518428671680621078381724386896258624262971787023054651438740237393
pubExp=INTEGER:65537
privExp=INTEGER:3998731487633352107852441255033768239881091376738602013454220231226719498
p=INTEGER:286748798713412687878508722355577911069
q=INTEGER:300290718931931563784555212798489747397
e1=INTEGER:79871076793700741133958703119866436054
e2=INTEGER:297452792678365151939346760860803354174
coeff=INTEGER:43340310015875206124799642386915239847
```
- Tiếp theo chúng ta sẽ tiếp tục sử dụng tool `openssl` để tạo ra `private_key` dưới format file `.der`.
```sh
openssl asn1parse -genconf config.conf -out privkey.der
```
<img src=assets/p5.png>

- Sau khi đã có file [privkey.der](solve/privkey.der), chúng ta có thể lấy được `private_key` từ trong file `.der`
```sh
openssl rsa -in privkey.der -inform der -text -check
```
<img src=assets/p6.png>

- Tiếp theo copy đoạn trong khung đỏ và save lại ta được file [privkey.pem](solve/privkey.pem) dưới định dạng `.pem` phổ biến và dễ đọc.
<img src=assets/p7.png>

- Giờ chúng ta có thể thử kiểm tra các tham số `p`, `q`, ... từ file `private_key` này nào:
```sh
openssl rsa -in privkey.pem -text -noout
``` 
<img src=assets/p8.png>

- File `private_key` đã có, giờ tiếp tục dùng file [privkey.pem](solve/privkey.pem) để lấy file `public_key` thôi:
```sh
openssl rsa -in privkey.pem  -pubout
```
<img src=assets/p9.png>

- Như các bạn đã thấy, nội dung trong file [pubkey.pem](solve/pubkey.pem) hoàn toàn khớp với file [public.pem](problem/public.pem) mà đề cho.


**P/S: Đến đây thì cũng như xong 1 writeup cho 1 challenge :khóc_ròng_icon**
