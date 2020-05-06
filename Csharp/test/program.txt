using System;
using System.Collections.Generic;
namespace test
//To jest pierwszy program jaki napisałem w C# poza Unity
//Testowany na mono w Manjaro Linux
{
    class Program
    {
        static string[] pierwiastki = {"H", "He", "Li", "Be", "B", "C",
              "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S",
              "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe",
              "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
              "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd",
              "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba",
              "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy",
              "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os",
              "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
              "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm",
              "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg",
              "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"};
        static List<string> mendalejew(string toChange)
        {
            List<string> res = new List<string>();
            int i = 0;
            //Sprawdz czy coś pasuje, jak tak to dopisz to res
            foreach (string x in pierwiastki) {
                i++;
                string pierwiastek = x.ToLower();
                if (toChange == pierwiastek){
                  res.Add(i.ToString());
                  //res.Add(x);
                }
                if (toChange.StartsWith(pierwiastek)){
                    //Sprawdz czy do tego co zostało coś pasuje
                    List<string> results = mendalejew(toChange.Substring(pierwiastek.Length));
                    foreach (string I in results){
                        res.Add(i + "*" + I);
                        //res.Add(x + I);
                    }
                }
            }
            return res;
        }

        static void Main(string[] args)
        {
            string dane = Console.ReadLine();
            string[] frazy = dane.Split(" ");
            List<List<string>> results = new List<List<string>>();
            foreach (string fraza in frazy){
                List<string> x = mendalejew(fraza.ToLower());
                results.Add(x);
            }
            string display = "";
            bool sukces = true;
            foreach (List<string> word in results){
                if (word.Count == 0) {
                  Console.WriteLine("Nie można zapisać frazy szyfrem mendelejewa, odkryj więcej pierwiastków");
                  sukces = false;
                }
                else{
                  display = display + "**" + word[0];
                }
            }
            if (sukces) {
              Console.WriteLine(display.Substring(2));
            }


        }
    }
}
