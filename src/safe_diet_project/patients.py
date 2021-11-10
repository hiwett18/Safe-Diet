

class PatientType:
    def __init__(self, hypertension_patient = 'hypertension patient', diabetic_patient= 'diabetic patient', kidney_patient ='kidney patient'):
        self.hypertension_patient = hypertension_patient
        self.diabetic_patient = diabetic_patient
        self.kidney_patient = kidney_patient

    
    def select_patient(self):
        while True: 
            b = input('Are you 1. hypertension patient, 2. diabetic patient, or 3. kidney patient? Please select your number(1-3): ')
            try: 
                val = int(b)
                if val > 0 and val < 4:
                    if val == 1:
                        return self.hypertension_patient
                    elif val == 2:
                        return self.diabetic_patient
                    elif val == 3:
                        return self.kidney_patient
                    break
                else:
                    print('Please try again')

            except ValueError:
                print("Choice must be a number, between 1-3")    
            
                
        
                

        

# p1 = PatientType()
# print(p1.select_patient())
            