import msgspec

"""
msgspec.Struct 是Python库msgspec中的一个核心类,用于定义高性能、结构化的数据模型。
它类似于 Python 的 dataclasses 或 Pydantic 的 BaseModel,
但设计初衷是为了在序列化（转换为 JSON、MessagePack 等格式）和反序列化（从这些格式转换回来）过程中实现极致的速度和低内存开销.
"""

# case1: 使用示例
class User(msgspec.Struct):
    name: str
    email: str
    age: int

# 1.创建一个User实例
user = User(name="Alice", email="alice@example.com", age=30)
user.age = 31

# 2.序列化为JSON字节串
json_data = msgspec.json.encode(user)
print(json_data)  # 输出: b'{"name":"Alice","email":"alice@example.com","age":31}'

# 3.从JSON字节串反序列化回User对象
decoded_user = msgspec.json.decode(json_data, type=User)
print(decoded_user)  # 输出: User(name='Alice', email='alice@example.com', age=30)

# case2: 使用冻结（不可变）结构体
class Config(msgspec.Struct, frozen=True):
    api_key: str
    timeout: int

config = Config(api_key="secret-key", timeout=60)
# config.api_key = "new-key" # 这一行代码会报错,因为Config是不可变的

json_data = msgspec.json.encode(config)
print(json_data)  # 输出: b'{"api_key":"secret-key","timeout":60}'

decoded_config = msgspec.json.decode(json_data, type=Config)
print(decoded_config)  # 输出: Config(api_key='secret-key', timeout=60)