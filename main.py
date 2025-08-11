
import mysql.connector as mydb

from tkinter import *
from tkinter import ttk

con = mydb.connect(
    host='localhost',
    user='root',
    password='root',
    database='mini_proj_db',
    autocommit=True
)

if con.is_connected():
    print('Connection Successful!')
else:
    print('Connection Unsuccessful!')

cur = con.cursor()


def login_window():
    def cred_check():
        inp1 = entry_id.get()
        inp2 = entry_pwd.get()
        validity = 0
        s1 = 'SELECT * FROM  login_creds;'
        cur.execute(s1)
        data = cur.fetchall()
        for i in data:
            if inp1 in i and inp2 in i:
                working_interface()
                validity += 1
        if validity == 0:
            output_msg = f'USERNAME or PASSWORD not Matching'
            output_text.configure(text=output_msg, fg='red')
        else:
            window1.destroy()

    def show_and_hide():
        if entry_pwd['show'] == '*':
            entry_pwd['show'] = ''
        else:
            entry_pwd['show'] = '*'

    window1 = Tk()
    window1.geometry('380x380')
    window1.title('ADMIN LOGIN')
    window1.configure(background='cyan')

    loginheading = Frame(
        master=window1,
        padx=10,
        pady=10,
        width=200,
        height=50,
        background='orange'
    )

    entryframe = Frame(
        master=window1,
        padx=10,
        pady=10,
        width=200,
        height=50,
        background='orange'
    )

    heading = Label(
        master=loginheading,
        text='ADMIN LOGIN',
        font=('Times', 20, 'bold'),
        background='pink',
        width=19,
        padx=10,
        pady=10
    )

    output_text = Label(
        master=window1,
        padx=10,
        pady=10,
        width=46,
        background='pink'
    )

    label_id = Label(
        master=entryframe,
        text='USERNAME',
        background='pink'
    )

    entry_id = Entry(
        master=entryframe,
        width=23
    )

    label_pwd = Label(
        master=entryframe,
        text='PASSWORD',
        background='pink'
    )

    entry_pwd = Entry(
        master=entryframe,
        width=23,
        show='*'
    )

    checkBox_pwd = Checkbutton(
        master=entryframe,
        text="show",
        command=show_and_hide
    )

    login_submit = Button(
        master=entryframe,
        height=2,
        width=10,
        text='LOGIN',
        command=lambda: [cred_check(), window1.destroy]
    )

    exit = Button(
        master=entryframe,
        text='EXIT',
        height=2,
        width=10,
        command=window1.destroy
    )

    loginheading.pack()
    entryframe.pack()
    heading.pack()
    output_text.pack()

    label_id.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    entry_id. grid(row=0, column=1, padx=10, pady=10, sticky='w')
    label_pwd.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    entry_pwd.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    checkBox_pwd.grid(row=1, column=2, padx=10, pady=10, sticky='w')
    login_submit.grid(row=2, column=1, padx=10, pady=10)
    exit.grid(row=3, column=1, padx=10, pady=10)


def working_interface():

    def display_all():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        s1 = 'SELECT * FROM employee;'

        cur.execute(s1)

        data = cur.fetchall()
        validity = 0
        for i in data:
            validity += 1

        if validity != 0:
            for record in data:
                treeview_button.insert(parent='', index='end', values=record)

            output_msg = "ALL DETAILS DISPLAYED"
            label_output.configure(text=output_msg)
        else:
            output_msg = "NO DETAILS TO DISPLAY"
            label_output.configure(text=output_msg)

    def add_details():
        validity = 0
        validity1 = 0

        a = entry_empno.get()
        b = entry_empname.get().strip().upper()
        c = entry_job.get().strip().upper()
        d = entry_hiredate.get()
        e = entry_sal.get()
        f = entry_deptno.get()
        g = b.replace(" ", "").lower()[0:3]+a+'@gmail.com'
        h = entry_phone.get()

        for i in range(1):

            if a == '' or b == '' or c == '' or d == '' or e == '' or f == '' or h == '':
                output_msg = "No Entry can be left Empty except MAIL ID"
                label_output.configure(text=output_msg)
                validity += 1
                break

            else:

                if len(str(a)) != 4 and str(a).isdigit != True:
                    output_msg = "Wrong Entry Made for Employee ID"
                    label_output.configure(text=output_msg)
                    validity += 1

                elif b.replace(" ", "").isalpha() != True:
                    output_msg = "Wrong Entry Made for Employee Name"
                    label_output.configure(text=output_msg)
                    validity += 1

                elif c.isalpha() != True:
                    output_msg = "Wrong Entry Made for Employee Job"
                    label_output.configure(text=output_msg)
                    validity += 1

                elif d.replace('-', '').isdigit() != True:
                    output_msg = "Wrong Entry Made for Hiredate, Format : [YYYY-MM-DD]"
                    label_output.configure(text=output_msg)
                    validity += 1

                elif str(e).count('.') != 0 or str(e).count('.') != 1 and str(e).replace('.', '').isdigit() != True:
                    output_msg = "Wrong Entry Made for Hiredate, Format : [YYYY-MM-DD]"
                    label_output.configure(text=output_msg)
                    validity += 1

                elif len(str(f)) != 2 and str(f).isdigit != True:
                    output_msg = "Wrong Entry Made for Department No."
                    label_output.configure(text=output_msg)
                    validity += 1

                elif len(h) != 10 and h.isdigit != True:
                    output_msg = "Wrong Entry Made for Phone No."
                    label_output.configure(text=output_msg)
                    validity += 1

        validity2 = 0
        if validity == 0:

            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data = cur.fetchall()
            for record in data:
                if int(a) == record[0]:
                    validity1 += 1
            for record1 in data:
                if h == record1[7]:
                    validity2 += 1

            if validity1 == 0:
                if validity2 == 0:
                    s1 = 'INSERT INTO employee\
                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s);'
                    val = [a, b, c, d, e, f, g, h]

                    cur.execute(s1, val)

                    output_msg = f'EMPLOYEE - ID : {a}, Employee : {b}, Job : {c}, Hiredate : {d}, Salary : {e}, Department : {f}, Phone No. : {h} - ADDED SUCCESSFULLY\n New Mail ID created : {g}'
                    label_output.configure(text=output_msg)
                else:
                    output_msg = f'Phone No. already Exists'
                    label_output.configure(text=output_msg)
            else:
                output_msg = f'Employee ID already Exists'
                label_output.configure(text=output_msg)

    def clear_space():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        output_msg = 'SPACE CLEARED'

        label_output.configure(text=output_msg)

    def change_details():

        inp = entry_empno.get()

        info1 = entry_job.get().strip().upper()
        info2 = entry_sal.get()
        info3 = entry_deptno.get()

        validity = 0
        s1 = 'SELECT * FROM employee;'
        cur.execute(s1)

        data = cur.fetchall()

        if inp == '':
            output_msg = "Enter Employee ID to be Changed"
            label_output.configure(text=output_msg)
        else:
            for record in data:
                if int(inp) == record[0]:
                    previousjob = record[2]
                    if info1 != '':
                        s2 = 'UPDATE employee SET job=%s WHERE empno=%s ;'
                        val = [info1, inp]
                        cur.execute(s2, val)
                        validity += 1
                        """if previousjob != info1:
                            s3 = 'UPDATE employee SET mail=%s WHERE empno=%s ;'
                            new_mail = record[1].replace(" ", "").lower(
                            )[0:3]+input+info1.lower()[0:3]+'@gmail.com'
                            val = [new_mail, inp]
                            cur.execute(s3, val)"""

                else:
                    output_msg = "Employee ID not found"
                    label_output.configure(text=output_msg)

            for record in data:
                if int(inp) == record[0]:
                    if info2 != '':
                        s2 = 'UPDATE employee SET sal=%s WHERE empno=%s ;'
                        val = [info2, inp]
                        cur.execute(s2, val)
                        validity += 1

            for record in data:
                if int(inp) == record[0]:
                    if info3.isdigit() != '':
                        s2 = 'UPDATE employee SET deptno=%s WHERE empno=%s ;'
                        val = [info3, inp]
                        cur.execute(s2, val)
                        validity += 1
                    else:
                        output_msg = "Wrong Entry for Department"
                        label_output.configure(text=output_msg)

            if validity > 0:
                output_msg = "Employee Details Successfully Changed"
                label_output.configure(text=output_msg)

            for i in treeview_button.get_children():
                treeview_button.delete(i)

            s1 = 'SELECT * FROM employee WHERE empno = %s;'
            val = [inp]

            cur.execute(s1, val)

            data = cur.fetchall()

            for record in data:
                treeview_button.insert(parent='', index='end', values=record)

    def search_empno():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_empno.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif len(inp) == 4 and inp.isdigit() == True:

            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for record in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE empno = %s;'
                val = [inp]

                cur.execute(s1, val)

                data = cur.fetchall()

                validity = 0
                for record in data:
                    treeview_button.insert(
                        parent='', index='end', values=record)
                    validity += 1
                    output_msg = f'Details of Employee ID Search for "{inp}"'
                    label_output.configure(text=output_msg)

                if validity != 0:
                    print()
                else:
                    output_msg = f'NO Details of Employee ID Search for "{inp}" Found'
                    label_output.configure(text=output_msg)

            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'
                label_output.configure(text=output_msg)

        else:
            output_msg = "INVALID ID ENTERED"
            label_output.configure(text=output_msg)

    def search_empname():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_empname.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif inp.replace(" ", '').isalpha() != True:
            output_msg = "INVALID NAME ENTERED"
            label_output.configure(text=output_msg)

        else:
            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for record in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE empname LIKE %s;'
                val = [inp+'%']

                cur.execute(s1, val)

                data = cur.fetchall()

                validity = 0
                for record in data:
                    treeview_button.insert(
                        parent='', index='end', values=record)
                    validity += 1
                    output_msg = f'Details of Employee Name Search for "{inp}"'
                    label_output.configure(text=output_msg)

                if validity != 0:
                    print()

                else:
                    output_msg = f'NO Details of Employee Name Search for "{inp}" Found'
                    label_output.configure(text=output_msg)

            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'
                label_output.configure(text=output_msg)

    def search_job():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_job.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif inp.isalpha() != True:
            output_msg = "INVALID JOB ENTERED"
            label_output.configure(text=output_msg)

        else:
            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for record in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE job LIKE %s;'
                val = [inp+'%']

                cur.execute(s1, val)

                data = cur.fetchall()

                validity = 0
                for record in data:
                    treeview_button.insert(
                        parent='', index='end', values=record)
                    validity += 1
                    output_msg = f'Details of Employee Job Search for "{inp}"'
                    label_output.configure(text=output_msg)

                if validity != 0:
                    print()
                else:
                    output_msg = f'NO Details of Employee Job Search for "{inp}" Found'
                    label_output.configure(text=output_msg)

            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'
                label_output.configure(text=output_msg)

    def search_hiredate():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_hiredate.get()
        inp1 = inp.replace('-', '')

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif inp1.isdigit() != True:
            output_msg = "INVALID HIREDATE ENTERED"
            label_output.configure(text=output_msg)

        else:

            if len(inp) <= 10 and len(inp) >= 4:
                s2 = 'SELECT * FROM employee;'
                cur.execute(s2)
                data1 = cur.fetchall()
                validity1 = 0
                for record in data1:
                    validity1 += 1

                if validity1 != 0:
                    s1 = 'SELECT * FROM employee WHERE hiredate LIKE %s;'
                    val = [inp+'%']

                    cur.execute(s1, val)

                    data = cur.fetchall()

                    validity = 0
                    for record in data:
                        treeview_button.insert(
                            parent='', index='end', values=record)
                        validity += 1
                        output_msg = f'Details of Employee Hiredate Search for "{inp}"'
                        label_output.configure(text=output_msg)

                    if validity != 0:
                        print()
                    else:
                        output_msg = f'NO Details of Employee Hiredate Search for "{inp}" Found'
                        label_output.configure(text=output_msg)
                else:
                    output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'
                    label_output.configure(text=output_msg)

            else:
                output_msg = "INVALID HIREDATE ENTERED"
                label_output.configure(text=output_msg)

    def search_sal():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_sal.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif '.' in inp:
            inp1 = inp.replace('.', '')

            if inp1.isdigit() == True:

                s2 = 'SELECT * FROM employee;'
                cur.execute(s2)
                data1 = cur.fetchall()
                validity1 = 0
                for i in data1:
                    validity1 += 1

                if validity1 != 0:
                    s1 = 'SELECT * FROM employee WHERE sal = %s;'
                    val = [inp]
                    cur.execute(s1, val)
                    data = cur.fetchall()
                    validity = 0
                    for record in data:
                        validity += 1

                    if validity != 0:
                        for record in data:
                            treeview_button.insert(
                                parent='', index='end', values=record)
                            output_msg = f'Details of Employee Salary Search for "{inp}"'
                            label_output.configure(text=output_msg)

                    else:
                        output_msg = f'NO Details of Employee Salary Search for "{inp}" Found'
                        label_output.configure(text=output_msg)
                else:
                    output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'

                    label_output.configure(text=output_msg)
            else:
                output_msg = "INVALID INPUT"
                label_output.configure(text=output_msg)
        else:
            if inp.isdigit() == True:

                s2 = 'SELECT * FROM employee;'
                cur.execute(s2)
                data1 = cur.fetchall()
                validity1 = 0
                for i in data1:
                    validity1 += 1

                if validity1 != 0:
                    s1 = 'SELECT * FROM employee WHERE sal = %s;'
                    val = [inp]
                    cur.execute(s1, val)
                    data = cur.fetchall()
                    validity = 0
                    for record in data:
                        validity += 1

                    if validity != 0:
                        for record in data:
                            treeview_button.insert(
                                parent='', index='end', values=record)
                            output_msg = f'Details of Employee Salary Search for "{inp}"'
                            label_output.configure(text=output_msg)
                    else:
                        output_msg = f'NO Details of Employee Salary Search for "{inp}" Found'

                        label_output.configure(text=output_msg)
                else:
                    output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'

                    label_output.configure(text=output_msg)
            else:
                output_msg = "INVALID INPUT"
                label_output.configure(text=output_msg)

    def search_deptno():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_deptno.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif inp.isdigit() != True:
            output_msg = "INVALID DEPATMENT NO. ENTERED"
            label_output.configure(text=output_msg)

        else:
            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for record in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE deptno = %s;'
                val = [inp]

                cur.execute(s1, val)

                data = cur.fetchall()

                for record in data:
                    treeview_button.insert(
                        parent='', index='end', values=record)

                validity = 0
                if len(inp) == 2:
                    for record in data:
                        treeview_button.insert(
                            parent='', index='end', values=record)
                        validity += 1
                        output_msg = f'Details of Department No. for "{inp}"'
                        label_output.configure(text=output_msg)

                    if validity != 0:
                        print()
                    else:
                        output_msg = f'NO Details of Department No. Search for "{inp}" Found'
                        label_output.configure(text=output_msg)

                else:
                    output_msg = "INVALID DEPARTMENT NO. ENTERED"
                    label_output.configure(text=output_msg)

            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'
                label_output.configure(text=output_msg)

    def search_phone():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_phone.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif inp.isdigit() != True:
            output_msg = "INVALID DEPATMENT NO. ENTERED"
            label_output.configure(text=output_msg)

        else:
            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for record in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE phone = %s;'
                val = [inp]

                cur.execute(s1, val)

                data = cur.fetchall()

                validity = 0
                if len(inp) == 10:
                    for record in data:
                        treeview_button.insert(
                            parent='', index='end', values=record)
                        validity += 1
                        output_msg = f'Details of Phone No. for "{inp}"'
                        label_output.configure(text=output_msg)

                    if validity != 0:
                        print()
                    else:
                        output_msg = f'NO Details of Phone No. Search for "{inp}" Found'
                        label_output.configure(text=output_msg)

                else:
                    output_msg = "INVALID PHONE NO. ENTERED"
                    label_output.configure(text=output_msg)

            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'
                label_output.configure(text=output_msg)

    def search_mail():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_mail.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif '@gmail.com' not in inp:
            output_msg = "INVALID MAIL ID ENTERED"
            label_output.configure(text=output_msg)

        else:
            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for record in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE mail LIKE %s;'
                val = [inp+'%']

                cur.execute(s1, val)

                data = cur.fetchall()

                validity = 0
                for record in data:
                    treeview_button.insert(
                        parent='', index='end', values=record)
                    validity += 1
                    output_msg = f'Details of Mail ID Search for "{inp}"'
                    label_output.configure(text=output_msg)

                if validity != 0:
                    print()
                else:
                    output_msg = f'NO Details of Mail ID Search for "{inp}" Found'
                    label_output.configure(text=output_msg)

            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'
                label_output.configure(text=output_msg)

    def delete_empno():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_empno.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif len(inp) == 4 and inp.isdigit() == True:

            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for record in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE empno = %s;'
                val = [inp]
                cur.execute(s1, val)
                data = cur.fetchall()
                validity = 0
                for record in data:
                    validity += 1

                if validity != 0:
                    s2 = 'DELETE FROM employee WHERE empno = %s;'

                    cur.execute(s2, val)

                    output_msg = f'EMPLOYEE ID : {inp}, DELETED SUCCESSFULLY'

                    label_output.configure(text=output_msg)
                else:
                    output_msg = f'NO Details of Employee ID Search for "{inp}" Found'

                    label_output.configure(text=output_msg)
            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'

                label_output.configure(text=output_msg)

        else:
            output_msg = "INVALID INPUT"
            label_output.configure(text=output_msg)

    def delete_empname():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_empname.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif inp.replace(" ", '').isalpha() != True:
            output_msg = "INVALID NAME ENTERED"
            label_output.configure(text=output_msg)

        else:
            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for record in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE empname LIKE %s;'
                val = [inp+'%']
                cur.execute(s1, val)
                data = cur.fetchall()
                validity = 0
                for record in data:
                    validity += 1

                if validity != 0:
                    s1 = 'DELETE FROM employee WHERE empname LIKE %s;'
                    val = [inp+'%']

                    cur.execute(s1, val)

                    output_msg = f'EMPLOYEE NAME : {inp}, DELETED SUCCESSFULLY'
                    label_output.configure(text=output_msg)
                else:
                    output_msg = f'NO Details of Employee Name Search for "{inp}" Found'
                    label_output.configure(text=output_msg)
            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'
                label_output.configure(text=output_msg)

    def delete_job():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_job.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif inp.isalpha() != True:
            output_msg = "INVALID JOB ENTERED"
            label_output.configure(text=output_msg)

        else:
            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for record in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE job LIKE %s;'
                val = [inp+'%']
                cur.execute(s1, val)
                data = cur.fetchall()
                validity = 0
                for record in data:
                    validity += 1

                if validity != 0:
                    s1 = 'DELETE FROM employee WHERE job LIKE %s;'
                    val = [inp+'%']

                    cur.execute(s1, val)

                    output_msg = f'EMPLOYEE JOB : {inp}, DELETED SUCCESSFULLY'
                    label_output.configure(text=output_msg)
                else:
                    output_msg = f'NO Details of Employee Job Search for "{inp}" Found'
                    label_output.configure(text=output_msg)
            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'
                label_output.configure(text=output_msg)

    def delete_hiredate():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_hiredate.get()
        inp1 = inp.replace('-', '')

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif inp1.isdigit() != True:
            output_msg = "INVALID HIREDATE ENTERED"
            label_output.configure(text=output_msg)

        else:

            if len(inp) <= 10 and len(inp) >= 4:
                s2 = 'SELECT * FROM employee;'
                cur.execute(s2)
                data1 = cur.fetchall()
                validity1 = 0
                for record in data1:
                    validity1 += 1

                if validity1 != 0:
                    s1 = 'SELECT * FROM employee WHERE hiredate LIKE %s;'
                    val = [inp+'%']

                    cur.execute(s1, val)

                    data = cur.fetchall()

                    validity = 0
                    for record in data:
                        validity += 1

                    if validity != 0:
                        s1 = 'DELETE FROM employee WHERE hiredate LIKE %s;'
                        val = [inp+'%']

                        cur.execute(s1, val)

                        output_msg = f'EMPLOYEE HIREDATE : {inp}, DELETED SUCCESSFULLY'
                        label_output.configure(text=output_msg)
                    else:
                        output_msg = f'NO Details of Employee Hiredate Search for "{inp}" Found'
                        label_output.configure(text=output_msg)
                else:
                    output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'
                    label_output.configure(text=output_msg)
            else:
                output_msg = "INVALID HIREDATE ENTERED"
                label_output.configure(text=output_msg)

    def delete_sal():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_sal.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif '.' in inp:
            inp1 = inp.replace('.', '')

            if inp1.isdigit() == True:

                s2 = 'SELECT * FROM employee;'
                cur.execute(s2)
                data1 = cur.fetchall()
                validity1 = 0
                for i in data1:
                    validity1 += 1

                if validity1 != 0:
                    s1 = 'SELECT * FROM employee WHERE sal = %s;'
                    val = [inp]
                    cur.execute(s1, val)
                    data = cur.fetchall()
                    validity = 0
                    for record in data:
                        validity += 1

                    if validity != 0:
                        s2 = 'DELETE FROM employee WHERE sal = %s;'

                        cur.execute(s2, val)

                        output_msg = f'EMPLOYEE SALARY : {inp}, DELETED SUCCESSFULLY'

                        label_output.configure(text=output_msg)
                    else:
                        output_msg = f'NO Details of Employee Salary Search for "{inp}" Found'

                        label_output.configure(text=output_msg)
                else:
                    output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'

                    label_output.configure(text=output_msg)
            else:
                output_msg = "INVALID INPUT"
                label_output.configure(text=output_msg)
        else:
            if inp.isdigit() == True:

                s2 = 'SELECT * FROM employee;'
                cur.execute(s2)
                data1 = cur.fetchall()
                validity1 = 0
                for i in data1:
                    validity1 += 1

                if validity1 != 0:
                    s1 = 'SELECT * FROM employee WHERE sal = %s;'
                    val = [inp]
                    cur.execute(s1, val)
                    data = cur.fetchall()
                    validity = 0
                    for record in data:
                        validity += 1

                    if validity != 0:
                        s2 = 'DELETE FROM employee WHERE sal = %s;'

                        cur.execute(s2, val)

                        output_msg = f'EMPLOYEE SALARY : {inp}, DELETED SUCCESSFULLY'

                        label_output.configure(text=output_msg)
                    else:
                        output_msg = f'NO Details of Employee Salary Search for "{inp}" Found'

                        label_output.configure(text=output_msg)
                else:
                    output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'

                    label_output.configure(text=output_msg)
            else:
                output_msg = "INVALID INPUT"
                label_output.configure(text=output_msg)

    def delete_deptno():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_deptno.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif len(inp) == 2 and inp.isdigit() == True:

            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for record in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE deptno = %s;'
                val = [inp]
                cur.execute(s1, val)
                data = cur.fetchall()
                validity = 0
                for record in data:
                    validity += 1

                if validity != 0:
                    s2 = 'DELETE FROM employee WHERE deptno = %s;'

                    cur.execute(s2, val)

                    output_msg = f'DEPARTMENT NO. : {inp}, DELETED SUCCESSFULLY'

                    label_output.configure(text=output_msg)
                else:
                    output_msg = f'NO Details of DEPARTMENT NO. Search for "{inp}" Found'

                    label_output.configure(text=output_msg)
            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'

                label_output.configure(text=output_msg)

        else:
            output_msg = "INVALID INPUT"
            label_output.configure(text=output_msg)

    def delete_mail():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_mail.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif '@gmail.com' not in inp:
            output_msg = "INVALID MAIL ENTERED"
            label_output.configure(text=output_msg)

        else:
            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for i in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE mail LIKE %s;'
                val = [inp+'%']
                cur.execute(s1, val)
                data = cur.fetchall()
                validity = 0
                for record in data:
                    validity += 1

                if validity != 0:
                    s1 = 'DELETE FROM employee WHERE mail LIKE %s;'
                    val = [inp+'%']

                    cur.execute(s1, val)

                    output_msg = f'EMPLOYEE MAIL : {inp}, DELETED SUCCESSFULLY'
                    label_output.configure(text=output_msg)
                else:
                    output_msg = f'NO Details of Employee Mail Search for "{inp}" Found'
                    label_output.configure(text=output_msg)
            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'
                label_output.configure(text=output_msg)

    def delete_phone():

        for i in treeview_button.get_children():
            treeview_button.delete(i)

        inp = entry_phone.get()

        if inp == "":
            output_msg = "EMPTY ENTRY"
            label_output.configure(text=output_msg)

        elif len(inp) == 10 and inp.isdigit() == True:

            s2 = 'SELECT * FROM employee;'
            cur.execute(s2)
            data1 = cur.fetchall()
            validity1 = 0
            for record in data1:
                validity1 += 1

            if validity1 != 0:
                s1 = 'SELECT * FROM employee WHERE phone = %s;'
                val = [inp]
                cur.execute(s1, val)
                data = cur.fetchall()
                validity = 0
                for record in data:
                    validity += 1

                if validity != 0:
                    s2 = 'DELETE FROM employee WHERE phone = %s;'

                    cur.execute(s2, val)

                    output_msg = f'EMPLOYEE PHONE No. : {inp}, DELETED SUCCESSFULLY'

                    label_output.configure(text=output_msg)
                else:
                    output_msg = f'NO Details of Employee Phone Search for "{inp}" Found'

                    label_output.configure(text=output_msg)
            else:
                output_msg = f'EMPTY DATABASE : NOTHING TO BE DELETED'

                label_output.configure(text=output_msg)

        else:
            output_msg = "INVALID INPUT"
            label_output.configure(text=output_msg)

    main_window = Tk()
    main_window.geometry('1000x600')
    main_window.title("WORKFORCE TRACKER")
    main_window.configure(background='pink')

    frame1 = Frame(
        master=main_window,
        padx=10,
        pady=10,
        width=200,
        height=50,
        background='pink'
    )

    label_frame1 = LabelFrame(
        master=main_window,
        text='EMPLOYEE DETAILS',
        font=('Times', 15, 'underline'),
        padx=10,
        pady=10,
        background='pink'
    )

    label_frame2 = LabelFrame(
        master=main_window,
        text='DETAILS DISPLAY BAR',
        font=('Times', 15, 'underline'),
        padx=10,
        pady=10,
        background='pink'
    )

    label_frame3 = LabelFrame(
        master=main_window,
        text='FUNCTIONS',
        font=('Times', 15, 'underline'),
        padx=10,
        pady=10, background='pink'
    )

    label_output = Label(
        master=label_frame2,
        padx=10,
        pady=10,
        background='pink'
    )

    heading1 = Label(
        master=frame1,
        text='WORKFORCE TRACKER',
        font=('Times', 20, 'bold', 'underline'),
        background='pink',
        padx=10,
        pady=10
    )

    heading2 = Label(
        master=frame1,
        text='Jayantilal Ratilal & Co.',
        font=('Times', 20, 'bold', 'underline'),
        background='pink',
        padx=10,
        pady=10
    )

    label_empno = Label(
        master=label_frame1,
        text='Employee ID',
        background='pink'
    )

    entry_empno = Entry(
        master=label_frame1,
        width=23
    )

    label_empname = Label(
        master=label_frame1,
        text='Employee Name',
        background='pink'
    )

    entry_empname = Entry(
        master=label_frame1,
        width=23
    )

    label_job = Label(
        master=label_frame1,
        text='Employee Job',
        background='pink'
    )

    entry_job = Entry(
        master=label_frame1,
        width=23
    )

    label_hiredate = Label(
        master=label_frame1,
        text='Employee Hiredate',
        background='pink'
    )

    entry_hiredate = Entry(
        master=label_frame1,
        width=23
    )

    label_sal = Label(
        master=label_frame1,
        text='Employee Salary',
        background='pink'
    )

    entry_sal = Entry(
        master=label_frame1,
        width=23
    )

    label_deptno = Label(
        master=label_frame1,
        text='Department No',
        background='pink'
    )

    entry_deptno = Entry(
        master=label_frame1,
        width=23
    )

    label_mail = Label(
        master=label_frame1,
        text='Employee Mail-ID',
        background='pink',
    )

    entry_mail = Entry(
        master=label_frame1,
        width=23
    )

    label_phone = Label(
        master=label_frame1,
        text='Employee Phone No.',
        background='pink',
    )

    entry_phone = Entry(
        master=label_frame1,
        width=23
    )

    button_add_details = Button(
        master=label_frame3,
        text='Add Employee',
        width=20,
        command=add_details
    )

    button_dispaly_all = Button(
        master=label_frame3,
        text='Display All',
        width=20,
        command=display_all
    )

    button_clear_space = Button(
        master=label_frame3,
        text='Clear Space',
        width=20,
        command=clear_space
    )

    button_change_details = Button(
        master=label_frame3,
        text='Change Details',
        width=20,
        command=change_details
    )

    button_logout = Button(
        master=label_frame3,
        text='LOG OUT',
        width=9,
        height=3,
        command=lambda: [login_window(), main_window.destroy()]
    )

    button_search_empno = Button(
        master=label_frame3,
        text='Search [Employee ID]',
        width=20,
        command=search_empno
    )

    button_search_empname = Button(
        master=label_frame3,
        text='Search [Employee Name]',
        width=20,
        command=search_empname
    )

    button_search_job = Button(
        master=label_frame3,
        text='Search [Job]',
        width=20,
        command=search_job
    )

    button_search_hiredate = Button(
        master=label_frame3,
        text='Search [Hiredate]',
        width=20,
        command=search_hiredate
    )

    button_search_sal = Button(
        master=label_frame3,
        text='Search [Salary]',
        width=20,
        command=search_sal
    )

    button_search_deptno = Button(
        master=label_frame3,
        text='Search [Department No]',
        width=20,
        command=search_deptno
    )

    button_search_mail = Button(
        master=label_frame3,
        text='Search [Mail ID]',
        width=20,
        command=search_mail
    )

    button_search_phone = Button(
        master=label_frame3,
        text='Search [Phone No.]',
        width=20,
        command=search_phone
    )

    button_delete_empno = Button(
        master=label_frame3,
        text='Delete [Employee ID]',
        width=20,
        command=delete_empno
    )

    button_delete_empname = Button(
        master=label_frame3,
        text='Delete [Employee Name]',
        width=20,
        command=delete_empname
    )

    button_delete_job = Button(
        master=label_frame3,
        text='Delete [Job]',
        width=20,
        command=delete_job
    )

    button_delete_hiredate = Button(
        master=label_frame3,
        text='Delete [Hiredate]',
        width=20,
        command=delete_hiredate
    )

    button_delete_sal = Button(
        master=label_frame3,
        text='Delete [Salary]',
        width=20,
        command=delete_sal
    )

    button_delete_deptno = Button(
        master=label_frame3,
        text='Delete [Department No]',
        width=20,
        command=delete_deptno
    )

    button_delete_mail = Button(
        master=label_frame3,
        text='Delete [Mail ID]',
        width=20,
        command=delete_mail
    )

    button_delete_phone = Button(
        master=label_frame3,
        text='Delete [Phone No.]',
        width=20,
        command=delete_phone
    )

    treeview_button = ttk.Treeview(
        master=label_frame2,
        columns=(1, 2, 3, 4, 5, 6, 7, 8),
        show='headings'
    )

    treeview_button.heading(1, text='Employee ID')
    treeview_button.heading(2, text='Employee Name')
    treeview_button.heading(3, text='Job')
    treeview_button.heading(4, text='Hiredate')
    treeview_button.heading(5, text='Salary')
    treeview_button.heading(6, text='Department No')
    treeview_button.heading(7, text='Mail ID')
    treeview_button.heading(8, text='Phone Number')

    frame1.pack(padx=10, pady=10)

    label_frame2.pack(fill='both', expand='yes', padx=5, pady=5, side='bottom')
    label_frame1.pack(fill='both', expand='yes', padx=5, pady=5, side='left')
    label_frame3.pack(fill='both', expand='yes', padx=5, pady=5, side='right')

    label_output.pack(padx=10, pady=10)

    heading1.pack()
    heading2.pack()

    label_empno.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    entry_empno.grid(row=0, column=1, padx=10, pady=10, sticky='w')

    label_empname.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    entry_empname.grid(row=1, column=1, padx=10, pady=10, sticky='w')

    label_job.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    entry_job.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    label_hiredate.grid(row=1, column=2, padx=10, pady=10, sticky='w')
    entry_hiredate.grid(row=1, column=3, padx=10, pady=10, sticky='w')

    label_sal.grid(row=0, column=2, padx=10, pady=10, sticky='w')
    entry_sal.grid(row=0, column=3, padx=10, pady=10, sticky='w')

    label_deptno.grid(row=2, column=2, padx=10, pady=10, sticky='w')
    entry_deptno.grid(row=2, column=3, padx=10, pady=10, sticky='w')

    label_mail.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    entry_mail.grid(row=3, column=1, padx=10, pady=10, sticky='w')

    label_phone.grid(row=3, column=2, padx=10, pady=10, sticky='w')
    entry_phone.grid(row=3, column=3, padx=10, pady=10, sticky='w')

    button_add_details.grid(row=4, column=0,    padx=5, pady=5, sticky='w')
    button_dispaly_all.grid(row=4, column=1,    padx=5, pady=5, sticky='w')
    button_clear_space.grid(row=4, column=2,    padx=5, pady=5, sticky='w')
    button_change_details.grid(row=4, column=3, padx=5, pady=5, sticky='w')

    button_search_empno.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    button_delete_empno.grid(row=0, column=1, padx=5, pady=5, sticky='w')

    button_search_empname.grid(row=1, column=0, padx=5, pady=5, sticky='w')
    button_delete_empname.grid(row=1, column=1, padx=5, pady=5, sticky='w')

    button_search_job.grid(row=2, column=0, padx=5, pady=5, sticky='w')
    button_delete_job.grid(row=2, column=1, padx=5, pady=5, sticky='w')

    button_search_hiredate.grid(row=3, column=0, padx=5, pady=5, sticky='w')
    button_delete_hiredate.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    button_search_sal.grid(row=0, column=2, padx=5, pady=5, sticky='w')
    button_delete_sal.grid(row=0, column=3, padx=5, pady=5, sticky='w')

    button_search_deptno.grid(row=1, column=2, padx=5, pady=5, sticky='w')
    button_delete_deptno.grid(row=1, column=3, padx=5, pady=5, sticky='w')

    button_search_mail.grid(row=2, column=2,  padx=5, pady=5, sticky='w')
    button_delete_mail.grid(row=2, column=3,  padx=5, pady=5, sticky='w')

    button_search_phone.grid(row=3, column=2, padx=5, pady=5, sticky='w')
    button_delete_phone.grid(row=3, column=3, padx=5, pady=5, sticky='w')

    button_logout.grid(row=3, column=4, padx=5, pady=5, rowspan=2, sticky='w')

    treeview_button.pack(fill='both', expand='yes', padx=10, pady=10)


login_window()

mainloop()
