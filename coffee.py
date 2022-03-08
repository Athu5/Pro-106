import plotly.express as px
import csv

with open("cups of coffee vs hours of sleep.csv")as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Coffee", y = "sleep in hours" , color="week")

    fig.update_layout(autotypenumbers='convert types')

    fig.show()

