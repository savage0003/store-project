from django.shortcuts import render

def index(request):
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Catalog',
        'products': [
        {
            'image': '/static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Black hoodie with monograms adidas Originals',
            'price': '500 EUR',
            'description': "Soft fabric for sweatshirts. Style and comfort – it's a way of life."
        },
        {
            'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
            'name': 'Blue jacket The North Face',
            'price': '700 EUR',
            'description': "Smooth fabric. Waterproof coating. Light and warm down filling."
        },
         {
             'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'name': 'Brown sports oversized top ASOS DESIGN',
             'price': '100 EUR',
             'description': "Plush texture material. Comfortable and soft."
         },
        {   'image':'/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
            'name': 'Nike Heritage Backpack in Black',
            'price': '80 EUR',
            'description':'Thick fabric. Lightweight material.'

        },
        { 'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
          'name': 'Dr Martens 1461 Bex 3-Eye Platform Black Shoes',
          'price': '250 EUR',
          'description': 'Smooth leather upper. Natural material.'
        },
        { 'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
          'name': 'ASOS DESIGN wide leg formal trousers in navy',
          'price': '89 EUR',
          'description': 'Lightweight, stretchy seersucker textured fabric.'

        }
    ]
    }
    return render(request, 'products/products.html', context)
