#Lệnh uvicorn main:app đề cập đến:
#main: tệp main.py ("module" Python).
#app: đối tượng được tạo bên trong của main.py với dòng app = FastAPI().
#--reload: làm cho máy chủ khởi động lại sau khi thay đổi mã. Chỉ sử dụng để phát triển.


# FIRST STEPS


# from fastapi import FastAPI
# # FastAPI là một lớp kế thừa trực tiếp từ Starlette.
# app = FastAPI()
# # Ở đây biến 'app' sẽ là một "instance" của lớp FastAPI.
# @app.get("/")
# # Cú pháp đó @somethingtrong Python được gọi là "decorator" 
# # cho FastAPI biết rằng chức năng bên dưới tương ứng với đường dẫn / có thao tác get
# async def root():
#     return {"message": "Hello World"}


# PATH PARAMETERS


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}
# # Giá trị của tham số đường dẫn item_id sẽ được chuyển đến hàm của bạn dưới dạng đối số item_id

# # Giá trị được xác định trước:
# from enum import Enum

# from fastapi import FastAPI

# # Tạo một Enum class
# # Nhập Enum và tạo một lớp con kế thừa từ str và từ Enum.
# # Bằng cách kế thừa từ strcác tài liệu API sẽ có thể biết rằng các giá trị phải thuộc loại string và sẽ có thể hiển thị chính xác.

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# app = FastAPI()

# @app.get("/models/{model_name}")
# #Sau đó, tạo tham số đường dẫn với chú thích kiểu bằng cách sử dụng lớp enum bạn đã tạo ( ModelName)
# async def get_model(model_name: ModelName):
# #Bạn có thể so sánh nó với thành viên liệt kê trong enum đã tạo của bạn ModelName    
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
# # Lấy giá trị liệt kê
# # Bạn có thể lấy giá trị thực (a strtrong trường hợp này) bằng cách sử dụng model_name.valuehoặc nói chung là your_enum_member.value:
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#     return {"model_name": model_name, "message": "Have some residuals"}
# #Bạn có thể trả về các thành viên enum từ thao tác đường dẫn của mình , thậm chí được lồng trong phần thân JSON (ví dụ: a dict).


# QUERY PARAMETERS


# # Khi bạn khai báo các tham số chức năng khác không phải là một phần của tham số đường dẫn, 
# # chúng sẽ tự động được hiểu là tham số "truy vấn"
# from fastapi import FastAPI

# app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]
# # Truy vấn là tập hợp các cặp khóa-giá trị đi sau ? trong URL, được phân tách bằng các ký tự &

# #Thông số tùy chọn
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}
# #Trong trường hợp này, tham số chức năng q sẽ là tùy chọn và None là mặc định.

# # Chuyển đổi loại tham số truy vấn
# # Bạn cũng có thể khai báo kiểu bool và chúng sẽ được chuyển đổi:
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# # Nhiều tham số đường dẫn và truy vấn

# # Bạn có thể khai báo nhiều tham số đường dẫn và tham số truy vấn cùng lúc, FastAPI biết cái nào là cái nào.
# # Và bạn không cần phải khai báo chúng theo bất kỳ thứ tự cụ thể nào.
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# # Tham số truy vấn bắt buộc

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item
# # Ở đây tham số truy vấn needy là tham số truy vấn bắt buộc thuộc loại str

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_user_item(
#     item_id: str, needy: str, skip: int = 0, limit: int | None = None
# ):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item
# # Trong trường hợp này, có 3 tham số truy vấn:
# # needy, một yêu cầu str.
# # skip, một  int có giá trị mặc định là 0.
# # limit, một tùy chọn int.


# REQUEST BODY


# from fastapi import FastAPI

# # nhập BaseModeltừ pydantic
# from pydantic import BaseModel

# # khai báo mô hình dữ liệu của mình dưới dạng một lớp kế thừa từ BaseModel
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
# # Cũng giống như khi khai báo tham số truy vấn, khi thuộc tính model có giá trị mặc định thì không bắt buộc. 
# # Nếu không, nó là bắt buộc. Sử dụng None để làm cho nó chỉ là tùy chọn

# app = FastAPI()

# @app.post("/items/")
# # khai báo nó giống như cách bạn đã khai báo các tham số truy vấn và đường dẫn:
# # và khai báo kiểu của nó là kiểu bạn đã tạo, Item.
# async def create_item(item: Item):
#     return item

# # Sử dụng mô hình

# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# app = FastAPI()

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# # Yêu cầu nội dung + tham số đường dẫn

# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# app = FastAPI()

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# # Nội dung yêu cầu + đường dẫn + tham số truy vấn

# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# app = FastAPI()

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result


# # QUERY PARAMETERS and STRING VALIDATIONS


# # FastAPI cho phép bạn khai báo thông tin bổ sung và xác thực cho các tham số của mình.
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: str | None = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
# # FastAPI sẽ biết rằng giá trị của q không bắt buộc vì giá trị mặc định = None.

# # Xác thực bổ sung

# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/") 
# # Thêm Query vào Annotated trong tham số q
# # giá trị mặc định vẫn là None, vì vậy tham số vẫn là tùy chọn.
# async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # sử dụng Query() làm giá trị mặc định cho tham số chức năng của mình, đặt tham số max_length thành 50:
# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: str | None = Query(default=None, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
# # Như trong trường hợp này (không sử dụng Annotated), chúng ta phải thay thế giá trị mặc định Nonetrong hàm bằng Query(), 
# # bây giờ chúng ta cần đặt giá trị mặc định bằng tham số Query(default=None), 
# # nó phục vụ cùng mục đích xác định giá trị mặc định đó

# # Thêm biểu thức chính quy
# # có thể xác định một biểu thức chính quy mà tham số phải khớp:
# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None, Query(min_length=3, max_length=50, regex="^fixedquery$")
#     ] = None
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
# # Biểu thức chính quy cụ thể này kiểm tra xem giá trị tham số đã nhận:
# # ^: bắt đầu bằng ký tự sau, không có ký tự trước.
# # fixedquery: có giá trị chính xác fixedquery.
# # $: kết thúc ở đó, không còn ký tự nào sau fixedquery.

# # Giá trị mặc định
# # có thể sử dụng các giá trị mặc định khác với None

# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # Làm cho nó bắt buộc
# # Bắt buộc với Dấu ba chấm ( ...)

# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # bắt buộc với None

# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # Sử dụng Pydantic Required thay vì Ellipsis ( ...)

# from typing import Annotated

# from fastapi import FastAPI, Query
# from pydantic import Required

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Annotated[str, Query(min_length=3)] = Required):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # Danh sách tham số truy vấn / nhiều giá trị

# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query()] = None):
#     query_items = {"q": q}
#     return query_items

# # Danh sách tham số truy vấn/nhiều giá trị có giá trị mặc định

# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
#     query_items = {"q": q}
#     return query_items

# # Khai báo thêm siêu dữ liệu
# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#         ),
#     ] = None
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # Tham số bí danh
# # có thể khai báo một alias, và bí danh đó là những gì sẽ được sử dụng để tìm giá trị tham số:

# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # Thông số không dùng nữa
# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(
#             alias="item-query",
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#             max_length=50,
#             regex="^fixedquery$",
#             deprecated=True,
#         ),
#     ] = None
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # Loại trừ khỏi OpenAPI
# # Để loại trừ tham số truy vấn khỏi lược đồ OpenAPI đã tạo (và do đó, khỏi hệ thống tài liệu tự động), 
# # hãy đặt tham số include_in_schema của Query thành False:

# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None
# ):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     else:
#         return {"hidden_query": "Not found"}


# # PATH PARAMETERS AND NUMERIC VALIDATIONS


# # Import Path
# # nhập Path từ fastapi và nhập Annotated
# from typing import Annotated

# from fastapi import FastAPI, Path, Query

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(
# # khai báo tất cả các tham số giống như đối với Query
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# # Đặt hàng các tham số khi cần

# from typing import Annotated

# from fastapi import FastAPI, Path

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(
#     q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# # Xác thực số: lớn hơn hoặc bằng

# from typing import Annotated

# from fastapi import FastAPI, Path

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# # Xác thực số: lớn hơn và nhỏ hơn hoặc bằng

# from typing import Annotated

# from fastapi import FastAPI, Path

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
#     q: str,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# Xác nhận số: float, lớn hơn và nhỏ hơn

from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results