from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Load the data into a DataFrame
    df = pd.read_csv('SampleSuperstore.csv')

    # Create the dashboard layout
    plots = []

    profit_by_ship_mode = df.groupby('Ship Mode')['Profit'].sum().reset_index()
    ship_mode_bar = px.bar(profit_by_ship_mode, x='Ship Mode', y='Profit', title='Profit by Ship Mode')
    ship_mode_bar.update_layout(height=400)  # Customize the plot height
    plots.append(ship_mode_bar.to_html(full_html=False))

    profit_by_segment = df.groupby('Segment')['Profit'].sum().reset_index()
    segment_pie = px.pie(profit_by_segment, values='Profit', names='Segment', title='Profit by Segment')
    segment_pie.update_layout(height=400)  # Customize the plot height
    plots.append(segment_pie.to_html(full_html=False))

    profit_by_country_city = df.groupby(['Country', 'City'])['Profit'].sum().reset_index()
    top_10_country_city = profit_by_country_city.nlargest(10, 'Profit')
    country_city_bar = px.bar(top_10_country_city, x='Country', y='Profit', color='City', title='Top 10 Cities by Profit')
    country_city_bar.update_layout(height=400)  # Customize the plot height
    plots.append(country_city_bar.to_html(full_html=False))

    scatter_plot = px.scatter(df, x='Quantity', y='Profit', color='Discount', title='Profit vs. Quantity with Discount')
    scatter_plot.update_layout(height=400)  # Customize the plot height
    plots.append(scatter_plot.to_html(full_html=False))

    profit_by_region = df.groupby('Region')['Profit'].sum().reset_index()
    region_bar = px.bar(profit_by_region, x='Region', y='Profit', title='Profit by Region')
    region_bar.update_layout(height=400)  # Customize the plot height
    plots.append(region_bar.to_html(full_html=False))

    scatter_discount_profit = px.scatter(df, x='Discount', y='Profit', color='Region', title='Profit vs. Discount by Region')
    scatter_discount_profit.update_layout(height=400)  # Customize the plot height
    plots.append(scatter_discount_profit.to_html(full_html=False))

    profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()
    sunburst_chart = px.sunburst(profit_by_category, path=['Category'], values='Profit', title='Profit by Category')
    sunburst_chart.update_layout(height=400)  # Customize the plot height
    plots.append(sunburst_chart.to_html(full_html=False))

    profit_by_subcategory = df.groupby('Sub-Category')['Profit'].sum().reset_index()
    funnel_chart = px.funnel(profit_by_subcategory, x='Profit', y='Sub-Category', title='Profit by Sub-Category')
    funnel_chart.update_layout(height=400)  # Customize the plot height
    plots.append(funnel_chart.to_html(full_html=False))

    sales_by_country = df.groupby('Country')['Sales'].sum().reset_index()
    animated_bubble_map = px.scatter_geo(sales_by_country, locations='Country', locationmode='country names', size='Sales', title='Sales by Country')
    animated_bubble_map.update_layout(height=400)  # Customize the plot height
    plots.append(animated_bubble_map.to_html(full_html=False))

    # Render the template with all plots
    return render_template('dashboard.html', plot_html=plots)

if __name__ == '__main__':
    app.run(debug=True)


