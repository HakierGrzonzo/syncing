﻿using System;

namespace test
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
        static List<List> mendalejew(string toChange)
        {
            int i = 0;
            foreach (string x in pierwiastki) {
                i++;
                string pierwiastek = x.ToLower();
                if (toChange.StartsWith(pierwiastek)){
                    Console.WriteLine(i);
                    mendalejew(toChange.Substring(pierwiastek.Length));
                }
            }
            string X = "xd";
            return X;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string fraza = "ziemniaki";
            mendalejew(fraza);
        }
    }
}
