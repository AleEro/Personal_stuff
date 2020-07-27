# WHY
This stuff created for my friends from Stellaris Strateguim translation guild

# User Guide for Google_API.py:
- Create spreadsheet shortcut

    
    ss = Spreadsheet()


- Create table


    ss.create_table()


-  Load table

https://docs.google.com/spreadsheets/d/spreadsheet_id/edit#gid=0

    ss.get_table('spreadsheet_id')

- Get values


    ss.get_data('spreadsheet_id', tb_max=6, tb_min=16)


- Add values
    
    
    ss.prepare_setValue("C1", [['Аutomatic Script Update'],
                           ['Аutomatic Script Update'],
                           ['Аutomatic Script Update'],
                           ['Аutomatic Script Update'],
                           ['Аutomatic Script Update']])
    ss.runPrepared()

- Set values
    
    
    ss.prepare_setValues("B2:C3", [["This is B2", "This is C2"], ["This is B3", "This is C3"]])

- Set one value
    
    
    ss.prepare_setValue('C1', [['Аutomatic Script Update']])

- Add column
       
    
    ss.insert_dimension(2, 3)

- Add row    
    
    
    ss.insert_dimension(2, 3, dimension='ROWS')


- Change column width

    
    ss.prepare_setColumnWidth(0, 317)
    
- Accept changes
    
    
    ss.runPrepared()
    
- Share it with email


    ss.give_access(role='', email_address='')
