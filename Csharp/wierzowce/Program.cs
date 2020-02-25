// Zadanie #1, miejskie widoki, C#
// Działa na mono na Manjaro Linux
﻿using System;
using System.Collections.Generic;

namespace wierzowce
{
    static class extensions
    {
        private static Random rng = new Random();

        public static void Shuffle<T>(this IList<T> list)
        {
            int n = list.Count;
            while (n > 1) {
                n--;
                int k = rng.Next(n + 1);
                T value = list[k];
                list[k] = list[n];
                list[n] = value;
            }
        }
    }
    class Program
    {
        static List<int> Reverse(List<int> list)
        {
          // Odwróć Liste
          list.Reverse();
          return list;
        }
        static List<int> GetCollumn(List<List<int>> array, int num)
        {
          // Zwróć kolumne z Listy List
          List<int> result = new List<int>();
          foreach (List<int> row in array) {
            result.Add(row[num]);
          }
          return result;
        }
        static void PrintArray(List<List<int>> array)
        {
          // Wypisz dowolny List<List<int>>
          foreach (List<int> x in array) {
            foreach (int y in x) {
              Console.Write(y);
            }
          Console.WriteLine();
          }
        }
        static List<List<int>> GenerateArray()
        {
          // Bazowa Tablica
          List<List<int>> result = new List<List<int>>{
            new List<int> {1,2,3,4,5},
            new List<int> {5,1,2,3,4},
            new List<int> {4,5,1,2,3},
            new List<int> {3,4,5,1,2},
            new List<int> {2,3,4,5,1}
          };
          // Potasuj wiersze w tablicy
          result.Shuffle();
          // Obróć tablice
          List<List<int>> rotated = new List<List<int>>();
          for (int i = 0; i < 5; i++) {
            rotated.Add(GetCollumn(result, i));
          }
          // potasuj byłe kolumny
          rotated.Shuffle();
          return rotated;
        }
        static int ileWidac(List<int> dane)
        {
          int prevMax = 0;
          int ileWidac = 0;
          foreach (int wysokosc in dane) {
            if (wysokosc > prevMax) {
              ileWidac++;
              prevMax = wysokosc;
            }
          }
          return ileWidac;
        }
        static void Main(string[] args)
        {
            // Wygeneruj tablice i tablice końcową
            List<List<int>> array = GenerateArray();
            List<List<int>> result = new List<List<int>>();
            // Dodaj 0 w pozycji [0][0]
            result.Add(new List<int> {0});
            for (int i = 0; i < array.Count; i++) {
              // Oblicz widoczność w wierszu [0]
              result[0].Add(ileWidac(GetCollumn(array, i)));
            }
            foreach (List<int> row in array) {
              // Oblicz widoczność dla wierszy z obu stron
              List<int> addable = new List<int>();
              addable.Add(ileWidac(row));
              foreach (int i in row) {
                addable.Add(i);
              }
              addable.Add(ileWidac(Reverse(row)));
              result.Add(addable);
            }
            // Dodaj zero dla ostatniego wiersza
            result.Add(new List<int> {0});
            for (int i = 0; i < array.Count; i++) {
              // Oblicz ostatni wiersz
              result[6].Add(ileWidac(Reverse(GetCollumn(array, i))));
            }
            // Dodaj brakujące zera
            result[0].Add(0);
            result[6].Add(0);
            // napraw błąd
            result[6] = Reverse(result[6]);
            // Wypisz
            PrintArray(result);
        }
    }
}
