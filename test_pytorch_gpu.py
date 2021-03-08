import torch
if torch.cuda.is_available():
    device = torch.cuda.current_device()
    print('Found GPU {} at: /device:GPU:{}'.format(torch.cuda.get_device_name(device), device))
else:
    print('GPU not available')