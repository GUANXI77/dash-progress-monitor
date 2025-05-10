import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import datetime

# Cleaned and corrected task schedule data
schedule_data = {
    "Umbau Absturzsicherung DG für Ebener": {
        "Start_Date": "2025-04-23",
        "Duration": 1,
        "End_Date": "2025-04-24",
        "Progress": 100
    },
    "Ertüchtigung Notentwässerung + NRWG": {
        "Start_Date": "2025-04-22",
        "Duration": 1,
        "End_Date": "2025-04-23",
        "Progress": 100
    },
    "Herstellung: Fassadenschutz": {
        "Start_Date": "2025-04-23",
        "Duration": 3,
        "End_Date": "2025-04-26",
        "Progress": 0
    },
    "Rückbau Betonfläche für Logistik Los 3": {
        "Start_Date": "2025-04-28",
        "Duration": 12,
        "End_Date": "2025-05-10",
        "Progress": 0
    },
    "Anlieferung - Eibringun über Röhre": {
        "Start_Date": "2025-04-28",
        "Duration": 1,
        "End_Date": "2025-04-29",
        "Progress": 0
    },
    "Sanierung Anschlussbewehrung U2": {
        "Start_Date": "2025-04-28",
        "Duration": 9,
        "End_Date": "2025-05-07",
        "Progress": 50
    },
    "Entfernen der bauseitigen Abdichtung an den Türleibungen": {
        "Start_Date": "2025-04-23",
        "Duration": 9,
        "End_Date": "2025-05-02",
        "Progress": 100
    },
    "Rückbau Kran ZZ": {
        "Start_Date": "2025-06-16",
        "Duration": 2,
        "End_Date": "2025-06-18",
        "Progress": 0
    },
    "Herstellung Rauchschutz im Entrauchungskanal": {
        "Start_Date": "2025-05-12",
        "Duration": 12,
        "End_Date": "2025-05-24",
        "Progress": 0
    },
    "Kette Verkehrsweg BSE": {
        "Start_Date": "2025-05-19",
        "Duration": 5,
        "End_Date": "2025-05-24",
        "Progress": 0
    },
    "Rückbau Gerüst Treppenturm EBM": {
        "Start_Date": "2025-05-05",
        "Duration": 5,
        "End_Date": "2025-05-10",
        "Progress": 0
    },
    "Aufbau Treppentürme (BSE 2x Ost 1x West)": {
        "Start_Date": "2025-05-12",
        "Duration": 5,
        "End_Date": "2025-05-17",
        "Progress": 0
    }
}

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Construction Progress Tracker"

# App layout
app.layout = html.Div([
    html.H1("📊 Construction Progress Dashboard", style={'textAlign': 'center'}),

    dcc.Dropdown(
        id='task-dropdown',
        options=[{'label': task, 'value': task} for task in schedule_data.keys()],
        value=list(schedule_data.keys())[0],
        style={'width': '80%', 'margin': 'auto'}
    ),

    html.Div(id='task-details', style={'textAlign': 'center', 'marginTop': 30}),

    dcc.Graph(id='progress-graph')
])

# Callback to update progress bar and task info
@app.callback(
    [Output('progress-graph', 'figure'),
     Output('task-details', 'children')],
    [Input('task-dropdown', 'value')]
)
def update_dashboard(selected_task):
    data = schedule_data[selected_task]
    progress = data["Progress"]

    figure = {
        'data': [{
            'x': [selected_task],
            'y': [progress],
            'type': 'bar',
            'name': 'Progress',
            'marker': {'color': 'green' if progress == 100 else 'orange'}
        }],
        'layout': {
            'title': f"Progress of Task: {selected_task}",
            'yaxis': {'title': 'Progress (%)', 'range': [0, 100]},
            'xaxis': {'title': 'Task'}
        }
    }

    details = html.Div([
        html.P(f"📅 Start Date: {data['Start_Date']}"),
        html.P(f"📆 End Date: {data['End_Date']}"),
        html.P(f"⏳ Duration: {data['Duration']} days"),
        html.P(f"✅ Progress: {data['Progress']}%")
    ])

    return figure, details

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
