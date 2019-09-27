## DCM 文件转换服务

#### 安装/启动

- 安装Python 3.7 环境
- 进入dcm-convert文件夹
- (可选)创建虚拟环境
- pip install -r requirements.txt
- python server.py

#### 配置

- 端口：更改 server.py 中的端口

#### 接口

- http://{ip}:{port}/convert?path={path}&file_name={file_name}&gray={gray}
- 例如：http://localhost:18080/convert?path=/Users/cheese/Src/PythonSrc/dmcm-convert/data&file_name=2.dcm&gray=false
- path为DCM文件路径。file_name为DCM文件名。gray为布尔值，是否输出灰度图。
- 返回值为输出的PNG文件路径。