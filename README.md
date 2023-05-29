# backend

## FastAPI

### 1. Khái niệm

FastApi là 1 web framework dùng để build API có hiệu năng cao, dễ học, đơn giản nhưng cũng hỗ trợ tốt cho việc làm sản phẩm.

Đặc điểm:

- Fast: Hiệu suất cao ngang với NodeJS và Go.

- Fast to code: Code nhanh hơn, tốc độ code các features tăng khoảng 200 đến 300%.

- Fewer bugs: do đơn giản nên giảm số bugs của developper đến 40%.

- Intuitive: hỗ trợ code dễ hơn với tự động gợi ý, debug cần ít thời gian hơn so với trước.

- Easy: được thiết kế sao cho dễ dùng dễ học.

- Short: Tối thiểu việc lặp code. Các tham số truyền vào có nhiều tính năng. Ít bugs.

- Robust: hiệu năng mạnh mẽ, có thể tương tác API qua docs.

### 2. Ưu điểm

- FastAPI xác thực kiểu dữ liệu ngay cả trong các yêu cầu JSON lồng nhau.

- Với FastAPI, dễ dàng trong việc xử lý ngoại lệ.

- FastAPI hỗ trợ mã không đồng bộ bằng cách sử dụng các từ khóa async/awaitPython.

- Việc kiểm tra các điểm cuối FastAPI thực sự đơn giản và có thể được thực hiện bằng cách sử dụng TestClient do FastAPI cung cấp.

- FastAPI có một nguồn tài liệu rất phong phú và giàu ví dụ , giúp mọi việc trở nên dễ dàng hơn.

- Bạn có thể dễ dàng triển khai ứng dụng FastAPI của mình thông qua Docker bằng cách sử dụng docker image do FastAPI cung cấp . Bạn cũng có thể triển khai nó lên AWS Lamdba bằng Mangum .

### 3. Nhược điểm

- Trong FastAPI, mọi thứ được gắn với FastAPI app. Vì vậy, tệp main.py có thể rất dễ trở nên rắc rối.

- FastAPI sử dụng Pydantic để xác thực yêu cầu. Quá trình này không phải lúc nào cũng rất trực quan và đôi khi nó yêu cầu bạn viết trình xác thực tùy chỉnh của riêng mình.

- Không có singleton trong Dependency Injection