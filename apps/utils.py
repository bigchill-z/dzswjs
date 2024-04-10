from rest_framework.response import Response


# 二次封装Response
class APIResponse(Response):

    def __init__(self, code=400, msg='ok', result=None, http_status=None, headers=None, exception=False,
                 **kwargs):
        # data的初始状态
        data = {
            'code': code,
            'msg': msg
        }
        # data的响应数据体
        if result is not None:
            data['data'] = result
            data['code'] = 200
        # data的其他数据
        data.update(kwargs)
        super().__init__(data=data, status=http_status, headers=headers, exception=exception)
