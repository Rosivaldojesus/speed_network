import plotly.offline as opy
import plotly.graph_objs as go
from .models import Servico

def plot1(self, **kwargs):
    context = super(Servico, self).get_context_data(**kwargs)

    x = [-2 ,0 ,4 ,6 ,7]
    y = [ 1,2,3,4,5,6,7]
    trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': "10"},
                        mode="lines",  name='1st Trace')

    data =go.Data([trace1])
    layout =go.Layout(title="Meine Daten", xaxis={'title' :'x1'}, yaxis={'title' :'x2'})
    figure =go.Figure(data=data ,layout=layout)
    div = opy.plot(figure, auto_open=False, output_type='div')

    context['graph'] = div

    return context