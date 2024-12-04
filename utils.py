from pathlib import Path

def save_chart(chart, name):
    
    path = f'charts/{name}.html'
    save_path = Path(path)

    chart.write_html(save_path)