import tkinter as tk
from tkinter import ttk, messagebox

class NeffAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Neff's Anterior Coefficient Analysis")
        self.root.geometry("800x700")
        
        # Set style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        self.style.configure('Result.TLabel', font=('Arial', 10, 'bold'), foreground='blue')
        self.style.configure('TNotebook', background='#f0f0f0')
        self.style.configure('TNotebook.Tab', font=('Arial', 10))
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_input_tab()
        self.create_info_tab()
        
    def create_input_tab(self):
        # Input tab
        input_tab = ttk.Frame(self.notebook)
        self.notebook.add(input_tab, text="Analysis Calculator")
        
        # Header
        header_frame = ttk.Frame(input_tab)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header_frame, text="Neff's Anterior Coefficient Analysis", style='Header.TLabel').pack()
        ttk.Label(header_frame, text="Calculate the anterior coefficient for occlusion assessment").pack()
        
        # Input frame
        input_frame = ttk.LabelFrame(input_tab, text="Tooth Width Measurements (in mm)", padding="15")
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Maxillary teeth (ideal values from Neff's studies)
        ttk.Label(input_frame, text="Maxillary Teeth", font=('Arial', 10, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky=tk.W)
        
        # Incisor width (ideal: 8.5 mm)
        ttk.Label(input_frame, text="Incisor Width (11, 21):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.max_incisor = tk.DoubleVar(value=8.5)
        ttk.Entry(input_frame, textvariable=self.max_incisor, width=8).grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Canine width (ideal: 7.6 mm)
        ttk.Label(input_frame, text="Canine Width (13, 23):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.max_canine = tk.DoubleVar(value=7.6)
        ttk.Entry(input_frame, textvariable=self.max_canine, width=8).grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Mandibular teeth (ideal values from Neff's studies)
        ttk.Label(input_frame, text="\nMandibular Teeth", font=('Arial', 10, 'bold')).grid(row=3, column=0, columnspan=2, pady=(10, 5), sticky=tk.W)
        
        # Incisor width (ideal: 5.0 mm)
        ttk.Label(input_frame, text="Incisor Width (31, 41):").grid(row=4, column=0, sticky=tk.W, padx=5, pady=2)
        self.mand_incisor = tk.DoubleVar(value=5.0)
        ttk.Entry(input_frame, textvariable=self.mand_incisor, width=8).grid(row=4, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Canine width (ideal: 6.5 mm)
        ttk.Label(input_frame, text="Canine Width (33, 43):").grid(row=5, column=0, sticky=tk.W, padx=5, pady=2)
        self.mand_canine = tk.DoubleVar(value=6.5)
        ttk.Entry(input_frame, textvariable=self.mand_canine, width=8).grid(row=5, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(input_tab)
        button_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Button(button_frame, text="Calculate", command=self.calculate).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset).pack(side=tk.LEFT, padx=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(input_tab, text="Analysis Results", padding="15")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Coefficient result
        ttk.Label(results_frame, text="Anterior Coefficient:", font=('Arial', 10, 'bold')).pack(anchor=tk.W)
        self.coefficient_result = tk.Text(results_frame, height=2, wrap=tk.WORD, font=('Arial', 10))
        self.coefficient_result.pack(fill=tk.X, pady=(0, 10))
        
        # Interpretation result
        ttk.Label(results_frame, text="Interpretation:", font=('Arial', 10, 'bold')).pack(anchor=tk.W)
        self.interpretation_result = tk.Text(results_frame, height=6, wrap=tk.WORD, font=('Arial', 10))
        self.interpretation_result.pack(fill=tk.X)
        
    def create_info_tab(self):
        # Information tab
        info_tab = ttk.Frame(self.notebook)
        self.notebook.add(info_tab, text="Information")
        
        # Text widget with scrollbar
        text_frame = ttk.Frame(info_tab)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        text_scroll = ttk.Scrollbar(text_frame)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        info_text = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=text_scroll.set, 
                          font=('Arial', 10), padx=10, pady=10)
        info_text.pack(fill=tk.BOTH, expand=True)
        
        text_scroll.config(command=info_text.yview)
        
        # Add information content
        info_content = """NEFF'S ANTERIOR COEFFICIENT ANALYSIS INFORMATION

Measurement Instructions:
1. Measure the mesiodistal width of each tooth at its greatest contour
2. Use a digital caliper or Boley gauge for accurate measurements
3. Record to the nearest 0.1 mm
4. Measure both left and right teeth and sum the widths

Parameters:
- Maxillary Teeth: Central incisors (11,21) and canines (13,23)
- Mandibular Teeth: Central incisors (31,41) and canines (33,43)
- Anterior Coefficient = (Mandibular Sum) / (Maxillary Sum)

Ideal Values (based on Neff's studies):
Maxillary Teeth:
- Central Incisors (11,21): 8.5 mm (range 7.5-9.5 mm)
- Canines (13,23): 7.6 mm (range 7.0-8.2 mm)

Mandibular Teeth:
- Central Incisors (31,41): 5.0 mm (range 4.5-5.5 mm)
- Canines (33,43): 6.5 mm (range 6.0-7.0 mm)

Ideal Anterior Coefficient:
- Normal range: 1.20 to 1.22
- Associated with normal overbite of approximately 20%

Interpretation Guidelines:
- Coefficient 1.20-1.22: Ideal relationship
- Coefficient < 1.20: May result in:
  - Excessive overbite
  - Deep bite tendencies
  - Anterior crowding
- Coefficient > 1.22: May result in:
  - Reduced overbite
  - Open bite tendencies
  - Anterior spacing

Clinical Significance:
- Helps predict overbite characteristics
- Useful for treatment planning in cases with:
  - Deep bites or open bites
  - Anterior crowding or spacing
  - Tooth-size discrepancies
- Particularly valuable for:
  - Early treatment planning
  - Space analysis
  - Extraction decisions

Technique Notes:
1. Measure multiple teeth when possible
2. Consider tooth morphology and wear patterns
3. Combine with other diagnostic tools (cephalometrics, study models)
4. Always verify clinically before making treatment decisions

Common Findings:
- High coefficients often seen with:
  - Small maxillary teeth
  - Large mandibular teeth
  - Open bite tendencies
- Low coefficients often seen with:
  - Large maxillary teeth
  - Small mandibular teeth
  - Deep bite tendencies
"""
        info_text.insert(tk.END, info_content)
        info_text.config(state=tk.DISABLED)
    
    def calculate(self):
        try:
            # Calculate sums
            max_sum = self.max_incisor.get() + self.max_canine.get()
            mand_sum = self.mand_incisor.get() + self.mand_canine.get()
            
            if max_sum == 0:
                raise ValueError("Maxillary sum cannot be zero")
                
            coefficient = mand_sum / max_sum
            
            # Interpretation
            interpretation = ""
            if 1.20 <= coefficient <= 1.22:
                interpretation = "IDEAL RELATIONSHIP (1.20-1.22)\n"
                interpretation += "• Predicts normal overbite of approximately 20%\n"
                interpretation += "• Balanced anterior tooth size relationship\n"
                interpretation += "• Minimal risk of bite depth issues"
            elif coefficient < 1.20:
                interpretation = f"BELOW IDEAL RANGE ({coefficient:.3f} < 1.20)\n"
                interpretation += "• May result in excessive overbite\n"
                interpretation += "• Potential for deep bite development\n"
                interpretation += "• Possible anterior crowding\n"
                interpretation += "• Consider maxillary tooth size reduction or mandibular augmentation"
            else:
                interpretation = f"ABOVE IDEAL RANGE ({coefficient:.3f} > 1.22)\n"
                interpretation += "• May result in reduced overbite\n"
                interpretation += "• Potential for open bite tendencies\n"
                interpretation += "• Possible anterior spacing\n"
                interpretation += "• Consider mandibular tooth size reduction or maxillary augmentation"
            
            # Display results
            self.coefficient_result.config(state=tk.NORMAL)
            self.coefficient_result.delete(1.0, tk.END)
            self.coefficient_result.insert(tk.END, f"{coefficient:.3f} (Ideal range: 1.20-1.22)")
            self.coefficient_result.config(state=tk.DISABLED)
            
            self.interpretation_result.config(state=tk.NORMAL)
            self.interpretation_result.delete(1.0, tk.END)
            self.interpretation_result.insert(tk.END, interpretation)
            self.interpretation_result.config(state=tk.DISABLED)
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except tk.TclError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields")
    
    def reset(self):
        # Reset to ideal values
        self.max_incisor.set(8.5)
        self.max_canine.set(7.6)
        self.mand_incisor.set(5.0)
        self.mand_canine.set(6.5)
        
        self.coefficient_result.config(state=tk.NORMAL)
        self.coefficient_result.delete(1.0, tk.END)
        self.coefficient_result.config(state=tk.DISABLED)
        
        self.interpretation_result.config(state=tk.NORMAL)
        self.interpretation_result.delete(1.0, tk.END)
        self.interpretation_result.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NeffAnalysisApp(root)
    root.mainloop()