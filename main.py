from tkinter import Tk, Canvas, Frame, BOTH
import re
import math

class App(Tk):
    
    def __init__(self, ecuation):
        self.ecuation = ecuation
        super().__init__()
        self.initUI()
        self.geometry('601x601')
        
    def initUI(self):
        canvas = Canvas(self)
        points = self.algebra_interpreter()
        canvas.create_line(0,301,601,301)
        canvas.create_line(301,0,301,601)
        print(points)
        for i in range(len(points)):

            if i == len(points)-1:
                continue

            canvas.create_line(301+list(points)[i], 301-list(points.values())[i], 301+list(points)[i+1], 301-list(points.values())[i+1])
        canvas.pack(fill = BOTH, expand = True)
    
    def algebra_interpreter(self):
        
        local_ecuation = self.ecuation.replace(" ", "")

        def evaluate_ecuation(clean_ecuation, number):
            clean_ecuation = clean_ecuation.replace("x", "("+str(number)+")")
            if "sin(" in clean_ecuation:
                for i in re.findall("sin\(.*\)", clean_ecuation): 
                    try:            
                        clean_ecuation = clean_ecuation.replace(i, str(math.sin(float(eval(i[:-1].replace("sin(",""))))))
                    except:
                        print("division by 0 in:", i[:-1].replace("sin(",""))
                        return None
            try:
                return eval(clean_ecuation)
            except:
                return None

        points = {}
        previous = None
        for i in range(301):
            if evaluate_ecuation(local_ecuation, (i-151)*2) == None:
                continue
            if evaluate_ecuation(local_ecuation, (i-151)*2) > 301 or evaluate_ecuation(local_ecuation, (i-151)*2) <-301:
                previous = evaluate_ecuation(local_ecuation, (i-151)*2)

            else:
                if previous != None:
                    points[(i-152)*2] = evaluate_ecuation(local_ecuation, (i-152)*2)
                    

                points[(i-151)*2] = evaluate_ecuation(local_ecuation, (i-151)*2)

            

        return points
            
            

if __name__ == "__main__":
    app = App("1/((x/100)**2)")
    app.algebra_interpreter()
    app.mainloop()

