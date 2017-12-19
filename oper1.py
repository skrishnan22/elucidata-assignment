import pandas as pd 
from zipfile import ZipFile
import os
import io

df = pd.read_excel('upload_files/mass_spec_data_assgnmnt.xlsx')

pc_df = df[(df['Accepted Compound ID'].str.endswith('PC',na=False)) & (df['Accepted Compound ID'].str[-3]!='L')]
pc_df.to_csv('PC.csv',index=False)

lpc_df = df[df['Accepted Compound ID'].str.endswith('LPC',na=False)]
lpc_df.to_csv('LPC.csv',index=False)


plasgn_df = df[df['Accepted Compound ID'].str.endswith('plasmalogen',na=False)]
plasgn_df.to_csv('Plasmalogen.csv',index=False)

zip_file_list = ['PC.csv','LPC.csv','Plasmalogen.csv']

def zip_files():
	download_file = io.BytesIO()
	with ZipFile(download_file,'w') as zip_file:
		for csv_file in zip_file_list:
			zip_file.write(csv_file)
			os.remove(csv_file) 
	#print(download_file.read())		
	return download_file.getvalue()

zipped_file = zip_files()
print(zipped_file.decode('utf-8'))



'''rounded_retention_time = df.apply(lambda row : round(row['Retention time (min)']),axis=1)
df.insert(2,'Rounded_Retention_Time',rounded_retention_time)
df.to_csv('rounded_Retention_Time.csv',index=False)'''
