import uuid


def shop_icon(instance, file_name: str):
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'
    return f'shop_icon/{file_name}'


def shop_image(instance, file_name: str):
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'
    return f'shop_image/{file_name}'
