def GetBr(n):
    GetBr=Toplevel(main)
    GetBr.title(u'')
    GetBr.geometry('400x460+800+10')
    txtNTB = Text(GetBr,height=15,width=37,font='Arial 14',wrap=WORD)
    txtNTB.pack()
    txtNTB.place(x=10,y=10)
    scbrNTB = Scrollbar(GetBr, orient="vertical")
    scbrNTB.pack()
    scbrNTB.place(x=386, y=150)
    scbrNTB['command'] = txtNTB.yview
    txtNTB['yscrollcommand'] = scbrNTB.set
    Briefsf=open('Briefs','r')
    Briefs=Briefsf.readlines()
    Briefsf.close
    for i in range(len(Briefs)):
        if (Briefs[i])==(str(n)+'O'+'\n'):
            break
    for k in range(len(Briefs)):
        if (Briefs[i])==('END'+str(n)+'\n'):
            break
    for l in range(i+1,k):
        txtNTB.insert(1.0,Briefs[l])
    def GetBrOk(i,k):
        Briefsf=open('Briefs','a')
        Briefs2=['']
        Briefs2.append(Briefs[0:i])
        Briefs2.append(txtNTB.get(1.0,END))
        Briefs2.append(Briefs[k:])
        for i in range(len(Briefs2)):
            Briefsf.write(str(Briefs2[i]))
        Briefsf.close()
        GetBr.destroy()
    btnGBO = Button(GetBr, 
             text="OK",
             bg="white",fg="black", command=lambda: GetBrOk(i,k))
    btnGBO.pack()
    btnGBO.place(x=350,y=420)
    
#
# Add new task window
#

def NewTask():
    NT=Toplevel(main)
    NT.title(u'Add New Task')
    NT.geometry('400x460+800+10')
#Types of task reading
    TTypesf=open('TTypes','r')
    TTypes=TTypesf.readlines()
    TTypesf.close()
    for i in range(len(TTypes)):
        TTypes[i]=(TTypes[i])[0:-1]
#       
#errors
    def ERRWN():
        lblERR=Label(NT, text=('Wrong task name'))
        lblERR.pack()
        lblERR.place(x=10, y=435)
    def ERRYY(NTYY,NTMM,NTDD):
        #print(NTYY, NTMM, NTDD)
        lblERR=Label(NT, text=('404: '+NTYY+'  year not found'))
        lblERR.pack()
        lblERR.place(x=10, y=435)
        entYY.delete(0,END)
        pass
    def ERRVY(NTYY,NTMM,NTDD):
        lblERR=Label(NT, text=('404: 29 february of '+NTYY+'  year not found'))
        lblERR.pack()
        lblERR.place(x=10, y=435)
        entYY.delete(0,END)
        pass
    def ERRM31(NTYY,NTMM,NTDD):
         lblERR=Label(NT, text=('404: 30 of '+NTMM+' month not found'))
         lblERR.pack()
         lblERR.place(x=10, y=435)
         entDD.delete(0,END)
         pass
    def ERRF28(NTYY,NTMM,NTDD):
         lblERR=Label(NT, text=('404: '+NTDD+' of february not found'))
         lblERR.pack()
         lblERR.place(x=10, y=435)
         entDD.delete(0,END)
         pass
    def ERRD32(NTYY,NTMM,NTDD):
        lblERR=Label(NT, text=('404: '+NTDD+'  day not found'))
        lblERR.pack()
        lblERR.place(x=10, y=435)
        entDD.delete(0,END)
        pass
    def ERRMM(NTYY,NTMM,NTDD):
        lblERR=Label(NT, text=('404: '+NTMM+'  month not found'))
        lblERR.pack()
        lblERR.place(x=10, y=435)
        entMM.delete(0,END)
        pass
    def ERRWE(NTYY,NTMM,NTDD):
        lblERR=Label(NT, text=('ERROR: Wrong Date'))
        lblERR.pack()
        lblERR.place(x=10, y=435)
        entDD.delete(0,END)
        entMM.delete(0,END)
        entYY.delete(0,END)
        pass
    
#////////////////////////////
    def NTClose():
        NT.destroy()
        pass
    
    def NTOk():
        NTDD=entDD.get()
        NTMM=entMM.get()
        NTYY=entYY.get()
        NTType=lsbNTTP.curselection()
        #print(TTypes[NTType[0]])
        #print(NTDD+' '+NTMM+' '+ NTYY)
        if(entNTN.get()==''):
            ERRWN()
        elif((NTDD=='')or(NTMM=='')or(NTYY=='')):
            ERRWE(NTYY,NTMM,NTDD)
        elif (((int(NTMM))<1)or((int(NTDD))<1)):
            ERRWE(NTYY,NTMM,NTDD)
        elif ((int(NTYY)) < 2018):
            ERRYY(NTYY,NTMM,NTDD)
        elif((not((int(NTYY)%4)and(not(int(NTYY)%100))or(int(NTYY)%400)))and(int(NTMM)==2)and(int(NTDD==29))):
            ERRVY(NTYY,NTMM,NTDD)
        elif(((int(NTMM)==4) or (int(NTMM)==6) or (int(NTMM)==9) or (int(NTMM)==11))and(int(NTDD)==31)):
            ERRM31(NTYY,NTMM,NTDD)
        elif((int(NTMM)==2)and(int(NTDD)>28)):
            ERRF28(NTYY,NTMM,NTDD)
        elif(int(NTDD)>31):
            ERRD32(NTYY,NTMM,NTDD)
        elif(int(NTMM)>12):
            ERRMM(NTYY,NTMM,NTDD)
        else:
             Tasksf=open('Tasks','r')
             TasksAr=Tasksf.readlines()
             ATasks.append(Task())
             Tasksf.close()
             TNum=0
             #print (TNum)
             ATasks[TNum].Tid=str(len(TasksAr)/10)
             ATasks[TNum].TName=entNTN.get()
             TTypesf=open('TTypes','r')
             TTypes=TTypesf.readlines()
             TTypesf.close()
             ATasks[TNum].TType=(lsbNTTP.get(ACTIVE))
             ATasks[TNum].TDD=NTDD
             ATasks[TNum].TMM=NTMM
             ATasks[TNum].TYY=NTYY
             ATasks[TNum].TImp=sclNTI.get()
             ATasks[TNum].TSolved=False
             Tasksf=open('Tasks','a')
             Tasksf.write(str(int(ATasks[TNum].Tid))+'Open'+'\n')
             Tasksf.write(ATasks[TNum].TName+'\n')
             Tasksf.write((ATasks[TNum].TType)+'\n')
             Tasksf.write(str(ATasks[TNum].TDD)+'\n')
             Tasksf.write(str(ATasks[TNum].TMM)+'\n')
             Tasksf.write(str(ATasks[TNum].TYY)+'\n')
             Tasksf.write(str(ATasks[TNum].TImp)+'\n')
             Tasksf.write(str(ATasks[TNum].TSolved)+'\n')
             Tasksf.write(str(ATasks[TNum].Tid)+'\n')
             Tasksf.write('END'+str(TNum)+'\n')
             Tasksf.close()
             Briefsf=open('Briefs','a')
             Briefsf.write(str(TNum)+'O'+'\n')
             Briefsf.write(txtNTB.get(1.0,END))
             Briefsf.write('END'+str(int(ATasks[TNum].Tid)-1)+'\n')
             Briefsf.close()
             NT.destroy()
             root.destroy()
             RootUpdate()
        pass
    
    lblNTN = Label(NT,text="Task name:")
    lblNTN.pack()
    lblNTN.place(x=10, y=10)

    NTName=""
    entNTN = Entry(NT,textvariable=NTName, width=35)
    entNTN.pack()
    entNTN.place(x=100,y=10)

    lblNTTP = Label(NT,text="Task type:")
    lblNTTP.pack()
    lblNTTP.place(x=10, y=40)

    NTType=-1
    lsbNTTP = Listbox(NT,selectmode="single", width=37, height=4)
    for i in range(len(TTypes)):
        lsbNTTP.insert(i, TTypes[i])
    lsbNTTP.pack()
    lsbNTTP.place(x=85, y=42)
    scbrNTTP = Scrollbar(NT, orient="vertical")
    scbrNTTP.pack()
    scbrNTTP.place(x=386, y=65)
    scbrNTTP['command'] = lsbNTTP.yview
    lsbNTTP['yscrollcommand'] = scbrNTTP.set
    
    lblNTDD = Label(NT,text="Day:")
    lblNTDD.pack()
    lblNTDD.place(x=10, y=130)

    NTDD=''
    entDD = Entry(NT, textvariable=NTDD, width=2)
    entDD.pack()
    entDD.place(x=45,y=130)

    lblNTMM = Label(NT,text="Month:")
    lblNTMM.pack()
    lblNTMM.place(x=70, y=130)

    NTMM=''
    entMM = Entry(NT, textvariable=NTMM, width=2)
    entMM.pack()
    entMM.place(x=120,y=130)

    lblNTYY = Label(NT,text="Year:")
    lblNTYY.pack()
    lblNTYY.place(x=140, y=130)

    NTYY=''
    entYY = Entry(NT, textvariable=NTYY, width=4)
    entYY.pack()
    entYY.place(x=180,y=130)

    lblNTTP = Label(NT,text="Importance:")
    lblNTTP.pack()
    lblNTTP.place(x=10, y=160)

    sclNTI = Scale(NT,orient=HORIZONTAL,length=282,from_=1,to=10,tickinterval=1,
               resolution=1)
    sclNTI.pack()
    sclNTI.place(x=100,y=160)
    NTImp = sclNTI.get()

    lblNTB = Label(NT, text="Brief:")
    lblNTB.pack()
    lblNTB.place(x=10,y=220)

    txtNTB = Text(NT,height=7,width=37,font='Arial 14',wrap=WORD)
    txtNTB.pack()
    txtNTB.place(x=10,y=250)
    scbrNTB = Scrollbar(NT, orient="vertical")
    scbrNTB.pack()
    scbrNTB.place(x=386, y=300)
    scbrNTB['command'] = txtNTB.yview
    txtNTB['yscrollcommand'] = scbrNTB.set
    NTBrief=txtNTB.get('1.0', END)

    btnNTC = Button(NT, #New task close
             text="Close",
             bg="white",fg="black", command=NTClose)
    btnNTC.pack()
    btnNTC.place(x=268,y=420)

    btnNTO = Button(NT, #New task ok
             text="OK",
             bg="white",fg="black", command=NTOk)
    btnNTO.pack()
    btnNTO.place(x=338,y=420)
    
    NT.resizable(False,False)
    NT.grab_set()
    NT.wait_window(NT)
#
# Settings window
#

def OpenSet():
    Set=Toplevel(main)
    Set.title(u'Settings')
    Set.geometry('400x460+800+10')
#del 
    def DelTT():
        DTType=lsbDTT.curselection()
        TTypesf=open('TTypes','r')
        TTypes=TTypesf.readlines()
        TTypesf.close()
        TTypesf=open('TTypes','w')
        for i in range(len(TTypes)):
            for j in range(len(DTType)):
                if(i!=DTType[j]):
                    TTypesf.write(TTypes[i])
        TTypesf.close()
        TTypes=[0]
        TTypesf=open('TTypes','r')
        TTypes=TTypesf.readlines()
        TTypesf.close()
        for i in reversed(lsbDTT.curselection()):
            lsbDTT.delete(i)
#Del
    def SetClose():
        Set.destroy()
        pass
    
    def SetOk():
        Set.destroy()
        pass

    def SetATT():
        TTypesf=open('TTypes','a')
        TTypesf.write(entATT.get()+'\n')
        TTypesf.close()
        entATT.delete(0,END)      
        TTypesf.close()
        Set.destroy()
        OpenSet()
    
    btnSetC = Button(Set, #Settings close
             text="Close",
             bg="white",fg="black", command=SetClose)
    btnSetC.pack()
    btnSetC.place(x=268,y=420)

    btnSetOk = Button(Set, #Settings OK
             text="OK",
             bg="white",fg="black", command=SetOk)
    btnSetOk.pack()
    btnSetOk.place(x=338,y=420)

    #
    lblATT = Label(Set, text="Add new type of task:")
    lblATT.pack()
    lblATT.place(x=10,y=10)

    ATType=""
    entATT = Entry(Set, width=46, textvariable=ATType)
    entATT.pack()
    entATT.place(x=10,y=40)
    
    btnATT = Button(Set, #add task type
             text="ADD",
             bg="white",fg="black", command=SetATT)
    btnATT.pack()
    btnATT.place(x=328,y=70)

    lblDTT = Label(Set, text="Delete type of task:")
    lblDTT.pack()
    lblDTT.place(x=10,y=100)

    TTypesf=open('TTypes','r')
    TTypes=TTypesf.readlines()
    TTypesf.close()
    for i in range(len(TTypes)):
        TTypes[i]=(TTypes[i])[0:-1]
    lsbDTT = Listbox(Set, width=46, height=4)
    for i in range(len(TTypes)):
        lsbDTT.insert(i, TTypes[i])
    lsbDTT.pack()
    lsbDTT.place(x=10, y=120)
    scbrDTT = Scrollbar(Set, orient="vertical")
    scbrDTT.pack()
    scbrDTT.place(x=384, y=145)
    scbrDTT['command'] = lsbDTT.yview
    lsbDTT['yscrollcommand'] = scbrDTT.set   

    btnDTT = Button(Set, #Settings OK
             text="Delete",
             bg="white",fg="black", command=DelTT)
    btnDTT.pack()
    btnDTT.place(x=310,y=200)
    
    #

    Set.resizable(False,False)
    Set.grab_set()
    Set.wait_window(Set)

#
#  Main window
#

from Tkinter import *
#!!!!!!!!!!!!!!!!!!!!!
def GTN():
    Tasksf=open('Tasks','r')
    Tasks=Tasksf.readlines()
    Tasksf.close()
    return (len(Tasks))/10


class Task:
        TName="Task Name"
        TType="Task Type"
        TDD=0
        TMM=0
        TYY=0
        TImp=0
        TSolved=False
        Tid=0
        def __init__(self):
            self.storage = {}
        def __setitem__(self, key, value):
            self.storage[key] = value
        def __getitem__(self, key):
            return self.storage[key]
        def PTSA (self):
            print(self.TName,self.TType,self.TTime,self.TImp,self.TSolved*"+"+(not(self.TSolved))*"-",self.Tid)
        
ATasks=[Task()]
#Tasks.append(Task())
#Tasks[1].TName="First task"
#Tasks[1].TType="Other"
#Tasks[1].TTime="2018/10/03"
#Tasks[1].TImp=5
#Tasks[1].TSolved=False
#Tasks[1].Tid=1
def CloseTM():
    root.destroy()
    k=0
    Tasksf=open('Tasks','w')
    for i in reversed (range(len(Tasks))):
        if (i%10==7):
            Tasks[i]=str(achbTS[k].get())+'\n'
            k+=1
    for i in range(len(Tasks)):
        Tasksf.write(Tasks[i])
    Tasksf.close()
    root.destroy()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def DelTasks():
    Tasksf=open('Tasks','w')
    for k in reversed(range(len(achbTD))):
        for i in (range(10)):
            if (achbTD[k].get()):
                    Tasks[k*10+i]=''
    for i in range(len(Tasks)):
        Tasksf.write(Tasks[i])
    Tasksf.close()
    root.destroy()
    RootUpdate()
#Types=["Work", "Study", "Other"]
# !!!!!!!!!!!!!!!!!!!!

TTypesf=open('TTypes','r')
TTypes=TTypesf.readlines()
TTypesf.close()
for i in range(len(TTypes)):
    TTypes[i]=(TTypes[i])[0:-1]
#!!!!!!!!!!!!!!!!!!!!
main=Tk()

#mainmainmain
#Tasks.clear()

#mainmainmain
global root
root=Toplevel(main)
root.title(u'TaskManager v1.0')
root.resizable(False, True)
Tasksf=open('Tasks', 'r')
Tasks=Tasksf.readlines()
Tasksf.close()
lblTTNN=Label(root, text="N")
lblTTNN.pack()
lblTTNN.place(x=10,y=10)
lblTTN=Label(root, text="Name of task")
lblTTN.pack()
lblTTN.place(x=60,y=10)
lblTTT=Label(main, text="Type of task")
lblTTT.pack()
lblTTT.place(x=200,y=10)
lblTTD=Label(root, text="Date")
lblTTD.pack()
lblTTD.place(x=340,y=10)
lblTTI=Label(root, text="Importance")
lblTTI.pack()
lblTTI.place(x=460,y=10)
lblTTS=Label(root, text="Solved")
lblTTS.pack()
lblTTS.place(x=590,y=10)
lblTTBW=Label(root, text="Get brief")
lblTTBW.pack()
lblTTBW.place(x=670,y=10)
lblTTDL=Label(root, text="Del")
lblTTDL.pack()
lblTTDL.place(x=750,y=10)
lblTNN=[Label()]
for i in reversed(range(len(Tasks))):
    if (i%10==8):
        lblNumb=Label(root,text=str(int((Tasks[i])[0:-1])+1))
        lblTNN.append(lblNumb)
        lblNumb.pack()
        lblNumb.place(x=10,y=len(lblTNN)*20-10)
lblTN=[Label()]
for i in reversed(range(len(Tasks))):
    if (i%10==1):
        lblName=Label(root,text=(Tasks[i])[0:-1])
        lblTN.append(lblName)
        lblName.pack()
        lblName.place(x=60,y=len(lblTN)*20-10)
lblTT=[Label()]
for i in reversed(range(len(Tasks))):
    if (i%10==2):
        lblType=Label(root,text=(Tasks[i])[0:-1])
        lblTT.append(lblType)
        lblType.pack()
        lblType.place(x=200,y=len(lblTT)*20-10)
lblTD=[Label()]
for i in reversed(range(len(Tasks))):
    if (i%10==3):
        lblDate=Label(root,text=(((Tasks[i])[0:-1])*(int(Tasks[i])>9)+('0'+((Tasks[i])[0:-1]))*(int(Tasks[i])<=9)+
                                  '.'+(((Tasks[i+1])[0:-1])*(int(Tasks[i+1])>9)+(('0'+(Tasks[i+1])[0:-1])*(int(Tasks[i+1])<=9)))+'.'+((Tasks[i+2])[0:-1])))
        lblTD.append(lblDate)
        lblDate.pack()
        lblDate.place(x=340,y=len(lblTD)*20-10)
lblTI=[Label()]
for i in reversed(range(len(Tasks))):
    if (i%10==6):
        lblImp=Label(root,text=(Tasks[i])[0:-1])
        lblTI.append(lblImp)
        lblImp.pack()
        lblImp.place(x=490+7*(int(Tasks[i])<=9),y=len(lblTI)*20-10)

m=0
achbTS=[BooleanVar()]
chbTS=[Checkbutton()]
for i in reversed(range(len(Tasks))):
    if (i%10==7):
        achbTS.append(BooleanVar())
        chbSol=Checkbutton(root,text='', variable=achbTS[m], onvalue=True, offvalue=False )
        chbTS.append(chbSol)
        achbTS[m].set((Tasks[i]=='True\n')*True+(Tasks[i]=='False\n')*False)
        m+=1
        chbSol.pack()
        chbSol.place(x=610,y=len(chbTS)*20-10)
m=0
achbTD=[BooleanVar()]
chbTD=[Checkbutton()]
for i in reversed(range(len(Tasks))):
    if (i%10==0):
        achbTD.append(BooleanVar())
        chbDel=Checkbutton(root,text='', variable=achbTD[m], onvalue=True, offvalue=False )
        chbTD.append(chbDel)
        achbTD[m].set((Tasks[i]=='True\n')*True+(Tasks[i]=='False\n')*False)
        m+=1
        chbDel.pack()
        chbDel.place(x=760,y=len(chbTD)*20-10)
root.geometry('800x'+str((len(Tasks))*2+80)+'+0+10')

btnNT = Button(root, #Add new task (make new task window)
            text="Delete",
            bg="white",fg="black", command=DelTasks)
btnNT.pack()
btnNT.place(x=490, y=(len(Tasks))*2+40)

btnNT = Button(root, #Add new task (make new task window)
            text="Close",
            bg="white",fg="black", command=CloseTM)
btnNT.pack()
btnNT.place(x=570, y=(len(Tasks))*2+40)

btnNT = Button(root, #Add new task (make new task window)
            text="Add",
            bg="white",fg="black", command=NewTask)
btnNT.pack()
btnNT.place(x=735, y=(len(Tasks))*2+40)
btnSet = Button(root, #Open settings (make settings window)
            text="Settings",
            bg="white",fg="black", command=OpenSet)
btnSet.pack()
btnSet.place(x=645, y=(len(Tasks))*2+40)
root.destroy()
def RootUpdate():
    global root
    root=Toplevel(main)
    root.title(u'TaskManager v1.0')
    root.resizable(False, True)
    Tasksf=open('Tasks', 'r')
    Tasks=Tasksf.readlines()
    Tasksf.close()
    lblTTNN=Label(root, text="N")
    lblTTNN.pack()
    lblTTNN.place(x=10,y=10)
    lblTTN=Label(root, text="Name of task")
    lblTTN.pack()
    lblTTN.place(x=60,y=10)
    lblTTT=Label(main, text="Type of task")
    lblTTT.pack()
    lblTTT.place(x=200,y=10)
    lblTTD=Label(root, text="Date")
    lblTTD.pack()
    lblTTD.place(x=340,y=10)
    lblTTI=Label(root, text="Importance")
    lblTTI.pack()
    lblTTI.place(x=460,y=10)
    lblTTS=Label(root, text="Solved")
    lblTTS.pack()
    lblTTS.place(x=590,y=10)
    lblTTBW=Label(root, text="Get brief")
    lblTTBW.pack()
    lblTTBW.place(x=670,y=10)
    lblTTDL=Label(root, text="Del")
    lblTTDL.pack()
    lblTTDL.place(x=750,y=10)
    lblTNN=[Label()]
    for i in reversed(range(len(Tasks))):
        if (i%10==8):
            lblNumb=Label(root,text=str(int((Tasks[i])[0:-1])+1))
            lblTNN.append(lblNumb)
            lblNumb.pack()
            lblNumb.place(x=10,y=len(lblTNN)*20-10)
    lblTN=[Label()]
    for i in reversed(range(len(Tasks))):
        if (i%10==1):
            lblName=Label(root,text=(Tasks[i])[0:-1])
            lblTN.append(lblName)
            lblName.pack()
            lblName.place(x=60,y=len(lblTN)*20-10)
    lblTT=[Label()]
    for i in reversed(range(len(Tasks))):
        if (i%10==2):
            lblType=Label(root,text=(Tasks[i])[0:-1])
            lblTT.append(lblType)
            lblType.pack()
            lblType.place(x=200,y=len(lblTT)*20-10)
    lblTD=[Label()]
    for i in reversed(range(len(Tasks))):
        if (i%10==3):
            lblDate=Label(root,text=(((Tasks[i])[0:-1])*(int(Tasks[i])>9)+('0'+((Tasks[i])[0:-1]))*(int(Tasks[i])<=9)+
                                      '.'+(((Tasks[i+1])[0:-1])*(int(Tasks[i+1])>9)+(('0'+(Tasks[i+1])[0:-1])*(int(Tasks[i+1])<=9)))+'.'+((Tasks[i+2])[0:-1])))
            lblTD.append(lblDate)
            lblDate.pack()
            lblDate.place(x=340,y=len(lblTD)*20-10)
    lblTI=[Label()]
    for i in reversed(range(len(Tasks))):
        if (i%10==6):
            lblImp=Label(root,text=(Tasks[i])[0:-1])
            lblTI.append(lblImp)
            lblImp.pack()
            lblImp.place(x=490+7*(int(Tasks[i])<=9),y=len(lblTI)*20-10)

    m=0
    achbTS=[BooleanVar()]
    chbTS=[Checkbutton()]
    for i in reversed(range(len(Tasks))):
        if (i%10==7):
            achbTS.append(BooleanVar())
            chbSol=Checkbutton(root,text='', variable=achbTS[m], onvalue=True, offvalue=False )
            chbTS.append(chbSol)
            achbTS[m].set((Tasks[i]=='True\n')*True+(Tasks[i]=='False\n')*False)
            m+=1
            chbSol.pack()
            chbSol.place(x=610,y=len(chbTS)*20-10)
    m=0
    achbTD=[BooleanVar()]
    chbTD=[Checkbutton()]
    for i in reversed(range(len(Tasks))):
        if (i%10==0):
            achbTD.append(BooleanVar())
            chbDel=Checkbutton(root,text='', variable=achbTD[m], onvalue=True, offvalue=False )
            chbTD.append(chbDel)
            achbTD[m].set((Tasks[i]=='True\n')*True+(Tasks[i]=='False\n')*False)
            m+=1
            chbDel.pack()
            chbDel.place(x=760,y=len(chbTD)*20-10)
    btnGB=[Button()]
    m=0
    for i in reversed(range(len(Tasks))):
        if (i%10==0):
            btnGetBr=Button(root,text=' + ',pady=1,padx=1,command=lambda: GetBr(m))
            btnGB.append(btnGetBr)
            m+=1
            btnGetBr.pack()
            btnGetBr.place(x=670,y=len(btnGB)*20-10)
    root.geometry('800x'+str((len(Tasks))*2+80)+'+0+10')

    btnNT = Button(root, #Add new task (make new task window)
                 text="Delete",
                 bg="white",fg="black", command=DelTasks)
    btnNT.pack()
    btnNT.place(x=490, y=(len(Tasks))*2+40)

    btnNT = Button(root, #Add new task (make new task window)
                 text="Close",
                 bg="white",fg="black", command=CloseTM)
    btnNT.pack()
    btnNT.place(x=570, y=(len(Tasks))*2+40)

    btnNT = Button(root, #Add new task (make new task window)
                 text="Add",
                 bg="white",fg="black", command=NewTask)
    btnNT.pack()
    btnNT.place(x=735, y=(len(Tasks))*2+40)

    btnSet = Button(root, #Open settings (make settings window)
                 text="Settings",
                 bg="white",fg="black", command=OpenSet)
    btnSet.pack()
    btnSet.place(x=645, y=(len(Tasks))*2+40)
main.withdraw()
RootUpdate()
main.mainloop()
#!!!!!!!!!!!!!!!!!!!!!!!!
#Tasks[1].PTSA()
#Tasks[0].PTSA()
#print(GTN())
#print(TTypes)
