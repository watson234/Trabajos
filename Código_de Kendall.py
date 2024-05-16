import plotly.express as px

data = {
    'Categorías': ['Películas', 'Películas', 'Películas', 'Películas', 'Películas', 'Películas', 'Películas',
                   'Películas'],
    'Subcategorías': ['Acción y Aventura', 'Anime', 'Ciencia Ficción', 'Clásicas', 'Comedia', 'Documentales',
                      'Stand Up', 'Drama'],
    'Espacio': [45.54, 99.41, 38.01, 39.79, 50.81, 169.43, 22.22, 140.93]  # Espacio usado en GB
}

fig = px.treemap(data,
                 path=['Categorías', 'Subcategorías'],
                 values='Espacio',
                 title='Uso de Espacio en Disco por Categoría de Películas')
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

fig.show()
