class MathUtil():
    @staticmethod
    def calculerMoyenne(nombres):
        
        return 0 if not nombres else sum(nombres)/len(nombres)
    
   
tabNombres = [10, 10, 10, 10]
moyenne = MathUtil.calculerMoyenne(tabNombres)

print(f"La moyenne de {tabNombres} est {moyenne}")