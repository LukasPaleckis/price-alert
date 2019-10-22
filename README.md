# Price-alert

Python projektas kuris leidžia sužinoti apie pasirinkto daikto kainos sumažėjimą iki nustatytosios.

Pasirinktoje el. parduotuvėje (kolkas topocentras.lt) išsirinkus norimą prekę (bandyta tik su nešiojamais kompiuteriais) būtų galima sužinoti kada prekės kaina sumažėtų, sumažėjus prekės kainai iki nustatytos kainos ateitų pranešimas į el. paštą apie sumažėjusią kainą su pasirinktos prekės nuoroda. Į programą būtų galimą įkeltį prekės nuorodą, el. paštą ir įrašyti kainą kurią pasiekus į nurodytą el. paštą atkeliautų pranešimas su pasirinkta prekės kaina. 

## Programa leidžia:
 - įrašyti el. paštą į kurį ateitų pranešimai, 
 - įkelti pasirinktos prekės nuorodą,
 - nustatyti kainą ir išsaugoti.

 ### Programos veiksmai:

 Įrašius pasirinktą kainą, programa vieną kartą per parą nuskaitytų el. parduotuvės įkeltą nuorodą taip patikrindama ar kaina nesumažėjo iki pasirinktos. Jei patikrinus kaina pasiekia įrašyta sumą, išsiunčiamas el. pranešimas ir programos darbas baigtas.

[nuoroda](github.com)
## Programos naudojimas

$ pip install -r requirements.txt

https://datatofish.com/python-script-windows-scheduler/