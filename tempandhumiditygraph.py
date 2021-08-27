

import plotly.graph_objects as go
import pandas as pd




df = pd.read_csv('/home/pi/data_log.csv')
df.columns = [col.replace(" ", "") for col in df.columns]



fig= go.Figure()


fig.add_trace(
	go.Scatter(x=list(df.Time),  y=list(df.Temperature)))
fig.add_trace(
        go.Scatter(x=list(df.Time),  y=list(df.Humidity)))



  

fig.update_layout(
	xaxis=dict(
          rangeselector=dict(
	         buttons=list([
		   dict(count=1,
		     step="month",
			stepmode="backward")
            ])
         ),
         rangeslider=dict(
           visible=True
          ),
        type="date"  
    )
)



fig.show()


