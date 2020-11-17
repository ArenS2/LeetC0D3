# Problem
```sh
The Rickshank Rickdemption
 179 (26)
reverse

Welcome to the Rick and Morty universe! The council of Ricks have sent an army of Mortys ready to arrest Rick and cancel the interdimensional cable tv. Defeat them all, reach the last level and try to win. To be fair, you have to have a very high IQ to win.
Author: @AntonioLic, @matpro
[WubbaLubbaDubDub]
```
# Solve

- Đây là 1 dạng đề **reversing**, chúng ta không cần connect đến server của họ nên có thể khẳng định `flag` nằm sẵn trong file mà họ đưa cho chúng ta rồi, chỉ là cách lấy flag như thế nào thôi. 
- Sau khi tải [file](problem/WubbaLubbaDubDub) này về thì biết được đây là 1 file thực thi ELF, khi chạy thì nó show ra 1 trò chơi, đại loại sẽ có rất nhiều vòng và khi thắng hết tất cả các vòng sẽ có flag.
<img src=assets/a1.png>

- Nếu theo lối coding thông thường (không bảo mật), chúng ta sẽ có 1 biến `check`, khi biến check đó thỏa mãn (sau khi đã vượt qua tất cả các màn) thì sẽ gọi hàm `win()` (chẳng hạn) để in ra `flag`. 
- Giờ thử tìm hàm `win()` đó nào. Vì file này không bị `stripped` nên các tên hàm và tên biến đều được giữ nguyên khi biên dịch. Đây chính là 1 trong những lợi thế vô cùng quan trọng khi debug. 
<img src=assets/a2.png>

Dùng **IDA** chúng ta dễ dàng nhận ra ngay 1 hàm có tên là `winFunc()` và khả năng rất cao đây chính là hàm in ra flag cho chúng ta.  
<img src=assets/a3.png>

- Nếu theo hướng đó, việc chúng ta cần làm rất đơn giản. Đổi 1 hàm trong main (điều kiện: hàm này phải chắc chắn được gọi) thành hàm `winFunc()`. Ở đây mình chọn hàm `menu()`.
<img src=assets/a4.png>

- Sau đó vào **Edit -> Patch Program -> Assemble** của **IDA** để thay đổi câu lệnh `call` đó. Và hàm main lúc này trở thành:
<img src=assets/a5.png>

- Sau đó Save lại [chương trình vừa được patch](solve/WubbaLubbaDubDub) và ra ngoài chạy lại chương trình đó và lấy được flag.
<img src=assets/a6.png>

**P/S: Bài này là bài dễ chẳng qua file này là file trò chơi nên nặng, nhiều hàm, phân tích lâu nên cũng không nhiều người làm :##**
