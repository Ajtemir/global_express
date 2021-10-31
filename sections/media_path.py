import uuid


def shop_icon(instance, file_name: str):
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'
    return f'shop_icon/{file_name}'


def shop_image(instance, file_name: str):
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'
    return f'shop_image/{file_name}'


def news_image(instance, file_name: str):
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'
    return f'news_image/{file_name}'


def about_us_image(instance, file_name: str):
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'
    return f'about_us_images/{file_name}'


def how_it_work_image(instance, file_name: str):
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'
    return f'how_it_work/{file_name}'


def partner_image(instance, file_name: str):
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'
    return f'partner/{file_name}'


def index_store_image(instance, file_name: str):
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.ext'
    return f'index_store_image/{file_name}'
