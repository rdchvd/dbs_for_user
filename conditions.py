
def cond(col_names, sql):
    
    conditions=[]
    col=""
    while True:
        while col.upper() not in col_names:
            col = input('Яка колонка має бути ключовою в умові: ')
        val = input_format('Яке значення (не) має бути встановлене в колонці: ')
        ans = input("Введіть ознаку порівняння - значення {0} має бути: \nрівне {1}(1)\nне рівне {1}(2)\nбільше(або рівне) {1}(3)\nменше(або рівне) {1}(4) \n>>".format(col, val))  
        if ans == '1' or ans == '2':
            col += " = "
        elif ans == '3':
            col += " >= " 
        else:
            col += " <= "

        if isinstance(val, str):
            col+=("'{0}'".format(val))
        else:
            col+=("{0}".format(val))
        
        if ans == '2':
            col = "not " +col

        conditions.append(col)
       
        ans = input("Ще одна умова?так/ні: ")
        if ans=='ні':
            break
        
    if len(conditions)>1:
        ans = input("Всі умови мають виконатись або хоча б одна з них?всі/одна: ")
        if ans.lower()=='всі':
            cond =  " AND ".join(conditions)
        else: 
            cond =  " OR ".join(conditions)
            
    else:
        cond = conditions[0]
        
    sql = sql+' WHERE ' + cond.upper()
    
    return sql

def input_format(st):
    a = input(st)

    try:
        a = int(a)

    except ValueError:
        if a.capitalize() in ['True', 'False']:
            a = bool(a.capitalize())
    return a