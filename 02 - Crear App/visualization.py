import altair as alt
import pandas as pd


def create_vis():
    df = pd.read_csv("dataset/dataset_ejemplos.csv")

    color_genero = alt.Color('genero', title='Género', scale=alt.Scale(domain=['M', 'H'], range=['#8624F5', '#1FC3AA']))

    df['n_noticias'] = df['n_noticias_HH'] + df['n_noticias_HM'] + df['n_noticias_MM']

    chart1 = alt.Chart(df).mark_point(filled=True, size=100).encode(
        x=alt.X('segundos_discursos', title='Cantidad de discursos'),
        y=alt.Y('n_noticias', title="Cantidad de noticias en que aparece"),
        color=color_genero,
        tooltip='nombre')
    chart2 = alt.Chart(df).mark_boxplot().encode(y=alt.Y('genero', title=None),
                                                 x=alt.X('efectividad_voto', title='Efectividad del voto'),
                                                 color=color_genero)

    chart3 = alt.Chart(df).mark_point(filled=True, size=100).encode(
        x=alt.X('segundos_discursos', title='Tiempo en segundos'),
        y=alt.Y('n_discursos', title='Cantidad de discursos'),
        color=color_genero, tooltip='nombre')

    df_noticias = df.melt(value_vars=['n_noticias_HH', 'n_noticias_HM', 'n_noticias_MM'],
                          id_vars=['nombre', 'genero', 'n_discursos', 'segundos_discursos', 'efectividad_voto',
                                   'n_noticias'],
                          var_name='tipo_noticia',
                          value_name='cantidad_apariciones')

    df_noticias['tipo_noticia'] = df_noticias['tipo_noticia'].str.replace('n_noticias_', '')
    df_noticias['tipo_noticia'] = (df_noticias['tipo_noticia']
                                   .str.replace('HH', 'Un género')
                                   .str.replace('MM', 'Un género')
                                   .str.replace('HM', 'Ambos Géneros'))

    chart4 = alt.Chart(df_noticias).mark_bar().encode(x=alt.X('genero', title=None),
                                                      y=alt.Y('sum(cantidad_apariciones)',
                                                              title='Cantidad de apariciones'),
                                                      facet=alt.Facet('tipo_noticia', title='Géneros por noticia'),
                                                      color=color_genero)

    template_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/vega@{vega_version}"></script>
        <script src="https://cdn.jsdelivr.net/npm/vega-lite@{vegalite_version}"></script>
        <script src="https://cdn.jsdelivr.net/npm/vega-embed@{vegaembed_version}"></script>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
              integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    </head>
    <body>
    <div class="container">
        <h1> Visualizaciones de la convención</h1>
        <p>Estas visualizaciones las creamos durante el taller de Plataforma Telar</p>
        <div class="row">
            <div class="col">
                <h3>¿Hay una relación entre cuánto habla los convencionales con la cantidad de veces que aparecen en los
                    medios?</h3>
                <div id="vis1"></div>
            </div>
            <div class="col">
                <h3>¿Cuál es la efectividad del voto de hombres versus mujeres?</h3>
                <div id="vis2"></div>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <h3>¿Las mujeres piden más o menos la palabra?</h3>
                <div id="vis3"></div>
            </div>

            <div class="col">
                <h3>¿Cómo es la aparición en los medios de comunicación?</h3>
                <div id="vis4"></div>
            </div>
        </div>
    </div>

    <script type="text/javascript">
      vegaEmbed('#vis1', {spec1}).catch(console.error);
      vegaEmbed('#vis2', {spec2}).catch(console.error);
      vegaEmbed('#vis3', {spec3}).catch(console.error);
      vegaEmbed('#vis4', {spec4}).catch(console.error);
    </script>
    </body>
    </html>

    """

    with open('templates/vis.html', 'w') as f:
        f.write(template_html.format(
            vega_version=alt.VEGA_VERSION,
            vegalite_version=alt.VEGALITE_VERSION,
            vegaembed_version=alt.VEGAEMBED_VERSION,
            spec1=chart1.to_json(indent=None),
            spec2=chart2.to_json(indent=None),
            spec3=chart3.to_json(indent=None),
            spec4=chart4.to_json(indent=None),
        ))
