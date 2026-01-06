import streamlit as st
import pandas as pd 

st.title("Manejo de Dataframes")
st.sidebar.title("Parámetros")

modulo = st.sidebar.selectbox("Seleccione un modulo",["Filtros","Consultas","Agrupaciones","Muestras"])
df = pd.read_csv("Datos/ds_salaries.csv")

if modulo == "Filtros":
	
	st.write(df)
	st.write("Columnas del dataframe",df.columns)

	lista_columnas = list(df.columns)
	seleccion_columnas = st.multiselect("Seleccione las columnas",lista_columnas)

	st.write(seleccion_columnas)

	ingreso_indice = st.number_input("Ingrese el valor del índice")

	df_filtro_1 = df.loc[int(ingreso_indice),seleccion_columnas]
	st.write(df_filtro_1)

	indice_columna = st.number_input("Ingrese el indice de la columna")
	indice_fila = st.number_input("Ingrese el indice de la fila")

	df_filtro_2 = df.iloc[int(indice_fila),int(indice_columna)]
	st.write(df_filtro_2)

elif modulo == "Consultas":

	consulta = st.text_input("Ingrese el query")

	try:
		df_query = df.query(consulta)
		st.write(df_query)
	except:
		st.write("Ingrese el query y presione enter")	

	consulta_coincidencia = st.text_input("Ingrese coincidencia")
	seleccion_columna = st.selectbox("Escoja una columna",list(df.columns))

	try:
		df_coincidencia = df[df[seleccion_columna].str.contains(consulta_coincidencia)]
		st.write(df_coincidencia)
	except:
		st.write("Ingrese la coincidencia")	

elif modulo == "Agrupaciones":

	lista_columnas = list(df.columns)
	seleccion_columnas = st.multiselect("Seleccione las columnas",lista_columnas)
	columna_cuantitativa = st.selectbox("Seleccione una columna columna cuantitativa", lista_columnas)
	df_agrupacion_promedio = df.groupby(seleccion_columnas)[columna_cuantitativa].mean()
	st.write(df_agrupacion_promedio)

elif modulo == "Muestras":

	muestra_aleatoria = df.sample(n=int(st.number_input("Ingrese un valor")),random_state=42)
	st.write(muestra_aleatoria)

	muestra_aleatoria_2 = df.sample(frac=float(st.number_input("Ingrese una fraccion")),random_state=42)
	st.write(muestra_aleatoria_2)