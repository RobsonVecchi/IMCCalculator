import tkinter as tk


def calculate_bmi():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        
        if altura <= 0:
            resultado_label.config(text="A altura deve ser maior que zero.", fg="red")
            return
        
        bmi = peso / (altura ** 2)
        
        resultado_label.config(text=f"Seu IMC é: {bmi:.2f}", fg="blue")
        
        # Interpretation of BMI
        if bmi < 17:
            interpretacao_label.config(text="Muito abaixo do peso", fg="gray")
        elif bmi <= 18.5:
            interpretacao_label.config(text="Abaixo do peso", fg="orange")
        elif bmi <= 24.9:
            interpretacao_label.config(text="Peso normal", fg="green")
        elif bmi <= 29.9:
            interpretacao_label.config(text="Acima do peso", fg="orange")
        elif bmi <= 34.9:
            interpretacao_label.config(text="Obesidade I", fg="red")
        elif bmi < 39.9:    
            interpretacao_label.config(text="Obesidade II", fg="red")
        else:
            interpretacao_label.config(text="Obesidade III", fg="red")
    
    except ValueError:
        resultado_label.config(text="Por favor, entre com valores numéricos para peso e altura.", fg="red")


#Window
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("300x220")

# Labels
label_peso = tk.Label(root, text="Digite seu peso (kg):")
label_peso.grid(row=0, column=0, padx=10, pady=10)

label_altura = tk.Label(root, text="Digite sua altura (m):")
label_altura.grid(row=1, column=0, padx=10, pady=10)

# Inputs
entry_peso = tk.Entry(root)
entry_peso.grid(row=0, column=1, padx=10, pady=10)

entry_altura = tk.Entry(root)
entry_altura.grid(row=1, column=1, padx=10, pady=10)

# Button
calculate_button = tk.Button(root, text="Calcular IMC", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Labels for displaying results
resultado_label = tk.Label(root, text="", fg="blue")
resultado_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

interpretacao_label = tk.Label(root, text="", fg="black")
interpretacao_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
