import tkinter as tk

def calculate_bmi(event=None):
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
            interpretacao_label.config(text="Muito abaixo do peso", fg="#808080")  # gray
        elif bmi <= 18.5:
            interpretacao_label.config(text="Abaixo do peso", fg="#FFA500")  # orange
        elif bmi <= 24.9:
            interpretacao_label.config(text="Peso normal", fg="#008000")  # green
        elif bmi <= 29.9:
            interpretacao_label.config(text="Acima do peso", fg="#FFA500")  # orange
        elif bmi <= 34.9:
            interpretacao_label.config(text="Obesidade I", fg="#FF0000")  # red
        elif bmi < 39.9:    
            interpretacao_label.config(text="Obesidade II", fg="#FF0000")  # red
        else:
            interpretacao_label.config(text="Obesidade III", fg="#FF0000")  # red
    
    except ValueError:
        resultado_label.config(text="Por favor, digite valores válidos sem vírgulas.", fg="red")


# Create the main application window
root = tk.Tk()
root.title("Calculadora de IMC")

# Styling
root.configure(bg="#f0f0f0")  # Light gray background color

# Labels
label_peso = tk.Label(root, text="Digite seu peso (kg):", bg="#f0f0f0", fg="#333333", font=("Helvetica", 12, "bold"))
label_peso.grid(row=0, column=0, padx=10, pady=10, sticky="w")

label_altura = tk.Label(root, text="Digite sua altura (m):", bg="#f0f0f0", fg="#333333", font=("Helvetica", 12, "bold"))
label_altura.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Inputs
entry_peso = tk.Entry(root, width=10, font=("Helvetica", 12))
entry_peso.grid(row=0, column=1, padx=10, pady=10)

entry_altura = tk.Entry(root, width=10, font=("Helvetica", 12))
entry_altura.grid(row=1, column=1, padx=10, pady=10)

# Button
calculate_button = tk.Button(root, text="Calcular IMC", command=calculate_bmi, bg="#008000", fg="white", font=("Helvetica", 12, "bold"))
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

#Enter
root.bind('<Return>', calculate_bmi)

# Labels for displaying results
resultado_label = tk.Label(root, text="", fg="blue", font=("Helvetica", 14, "bold"), bg="#f0f0f0", wraplength=300) 
resultado_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

interpretacao_label = tk.Label(root, text="", fg="black", font=("Helvetica", 12), bg="#f0f0f0")
interpretacao_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Configure row and column weights to expand labels and entry fields
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run the Tkinter event loop
root.mainloop()