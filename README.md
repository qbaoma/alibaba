# alibaba
淘宝编写思路

  本项目使用Python开发，使用了tornado 框架，为避免使用原生的sql语句，加快编程，使用了python orm库 SQLAlchemy（阻塞）。本项目使用tornado的安全cookie增强安全性。为提高横向扩展能力，本项目也模仿openstack，
采用模块的形式，表现为单独提供了认证模块myOuth。本项目大多数函数都使用了协程来支持异步函数。本项目也争
取实现RESTful API。本项目的前端部分比较简陋，并且为减少前端工作量，前后端并未通过json解耦，而是使用了
tornado的模板直接渲染出html，客户端扩展性不强。同时为了减少数据通信量部分使用了Ajax。
              
  python 典型web框架很多，为尽可能大得支持在线用户数，选择了非阻塞异步的 tornado框架，tornado并不会为每一个在线用户保持一个线程。Tornado uses a single-threaded event loop，故需要在编程过程中避免阻塞函数。
  
  详细说明请参考本目录下 淘宝编写思路与使用说明.pdf

