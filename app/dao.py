def get_categories():
    return [{
        "id": 1,
        "name" :"Mobile"
    },{
        "id": 2,
        "name": "Table"
    }]
def get_produce(key):
    produt = [{
        "id": 1,
        "name":"samsung",
        "price": 1000000,
        "img":"https://cdn.mobilecity.vn/mobilecity-vn/images/2022/09/w250/samsung-galaxy-s22-hong-cu.jpg.webp"
    },{
        "id": 2,
        "name": "iphone",
        "price": 1000000,
        "img": "https://cdn.mobilecity.vn/mobilecity-vn/images/2022/09/w250/samsung-galaxy-s22-hong-cu.jpg.webp"
    },{
        "id": 3,
        "name": "samsung A33",
        "price": 1000000,
        "img": "https://cdn.mobilecity.vn/mobilecity-vn/images/2022/09/w250/samsung-galaxy-s22-hong-cu.jpg.webp"
    },{
        "id": 4,
        "name": "samsung note",
        "price": 1000000,
        "img": "https://cdn.mobilecity.vn/mobilecity-vn/images/2022/09/w250/samsung-galaxy-s22-hong-cu.jpg.webp"
    },{
        "id": 5,
        "name": "iphone X",
        "price": 1000000,
        "img": "https://cdn.mobilecity.vn/mobilecity-vn/images/2022/09/w250/samsung-galaxy-s22-hong-cu.jpg.webp"
    },{
        "id": 6,
        "name": "iphone 5",
        "price": 1000000,
        "img": "https://cdn.mobilecity.vn/mobilecity-vn/images/2022/09/w250/samsung-galaxy-s22-hong-cu.jpg.webp"
    },{
        "id": 7,
        "name": "iphone SE",
        "price": 1000000,
        "img": "https://cdn.mobilecity.vn/mobilecity-vn/images/2022/09/w250/samsung-galaxy-s22-hong-cu.jpg.webp"

    }]
    if key:
            produt =[p for p in produt if p['name'].find(key)>=0]
    return produt