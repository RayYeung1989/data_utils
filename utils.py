# import torch
#
# # for循环转cuda计算
# def for_loop_to_cuda(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs).cuda()
#     return wrapper
#
# def cuda(x):
#     if torch.cuda.is_available():
#         x = x.cuda()
#     return x
#
# # 使用cuda编程进行for计算
# def cuda_for_loop(x):
#     if torch.cuda.is_available():
#         x = x.cuda()
#         for i in range(x.shape[0]):
#             x[i] = x[i].cuda()
#     return x
#
