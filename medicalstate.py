from tkinter import *
import numpy as np
import pandas as pd
import tkinter as tk 
from tkinter import ttk 


l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)
print(l2)

df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

print(df)

X= df[l1]

y = df[["prognosis"]]
print(y)
np.ravel(y)
print(y)


tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
print(y_test)


def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   
    clf3 = clf3.fit(X,y)


    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))


    psymptoms = [symp1.get(),symp2.get(),symp3.get(),symp4.get(),symp5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))


    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))


    psymptoms = [symp1.get(),symp2.get(),symp3.get(),symp4.get(),symp5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))


    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))


    psymptoms = [symp1.get(),symp2.get(),symp3.get(),symp4.get(),symp5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")


root = Tk()
root.configure(background='#2ab7ca')


Name = StringVar()


w2 = Label(root, justify=LEFT, text="AI MEDICAL SUPPORT",bg='#2ab7ca')
w2.config(font=("Courier New Baltic", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)



NameLb = Label(root, text="Name of the Patient",fg="yellow", bg="#0e9aa7", width=20)
NameLb.grid(row=6, column=0, pady=15)


S1Lb = Label(root, text="Symptom 1", fg="yellow", bg="#03396c", width=20)
S1Lb.grid(row=7, column=0, pady=10)

S2Lb = Label(root, text="Symptom 2", fg="yellow",bg="#03396c", width=20)
S2Lb.grid(row=8, column=0, pady=10)

S3Lb = Label(root, text="Symptom 3", fg="yellow", bg="#03396c", width=20)
S3Lb.grid(row=9, column=0, pady=10)

S4Lb = Label(root, text="Symptom 4", fg="yellow", bg="#03396c", width=20)
S4Lb.grid(row=10, column=0, pady=10)

S5Lb = Label(root, text="Symptom 5", fg="yellow",bg="#03396c", width=20)
S5Lb.grid(row=11, column=0, pady=10)

btn1 = Button(root, text="DecisionTree", command=DecisionTree,bg="#4279a3",fg="yellow",width=20)
btn1.grid(row=15, column=0, pady=10)

btn2= Button(root, text="Randomforest", command=randomforest,bg="green",fg="yellow",width=20)
btn2.grid(row=17, column=0, pady=10)

btn3= Button(root, text="NaiveBayes", command=NaiveBayes,bg="#d11141",fg="yellow",width=20)
btn3.grid(row=19, column=0, pady=10)

OPTIONS = sorted(l1)

NameEn = Entry(root,width= 30, textvariable=Name)
NameEn.grid(row=6, column=1)

n = tk.StringVar() 

o = tk.StringVar() 

p = tk.StringVar() 

q = tk.StringVar() 

r = tk.StringVar() 

symp1 = ttk.Combobox(root, width = 27,textvariable = n)
symp1.grid(row=7, column=1)
symp1['values']=OPTIONS

symp2 = ttk.Combobox(root, width = 27,textvariable = o)
symp2.grid(row=8, column=1)
symp2['values']=OPTIONS


symp3 = ttk.Combobox(root, width = 27,textvariable = p)
symp3.grid(row=9, column=1)
symp3['values']=OPTIONS


symp4 = ttk.Combobox(root, width = 27,textvariable = q)
symp4.grid(row=10, column=1)
symp4['values']=OPTIONS


symp5 = ttk.Combobox(root, width = 27,textvariable = r)
symp5.grid(row=11, column=1)
symp5['values']=OPTIONS




t1 = Text(root, height=1, width=40,fg="black")
t1.grid(row=15, column=1, padx=10)

t2 = Text(root, height=1, width=40,fg="black")
t2.grid(row=17, column=1 , padx=10)

t3 = Text(root, height=1, width=40,fg="black")
t3.grid(row=19, column=1 , padx=10)

root.mainloop()
