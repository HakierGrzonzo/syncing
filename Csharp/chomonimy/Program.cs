// Zadanie 4, chomonimy, C#
// Plik slownik.txt powinien być w katalogu w którym jest program
// Program tworzy nowe wątki
﻿using System;
using System.Collections.Generic;
using System.IO;


namespace chomonimy
{
  class Node
  {
    public char letter;
    public static List<Node> children = new List<Node>();
    public Node(char _letter)
    {
      letter = _letter;
    }
    public void add(string word)
    {
      if (letter != word[0] && word.Length == 1) {
        foreach (Node child in children) {
          if (child.letter == word[0]) {
            child.add(word.Substring(1));
            break;
          }
        }
      }
    }
    public bool isIn(string word)
    {
      if (word[0] == this.letter && word.Length == 1){
        return true;
      }
      foreach (Node child in children) {
        if (child.letter == word[0]) {
          return child.isIn(word.Substring(1));
        }
      }
      return false;
    }
  }
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Droga Politechniko, czy wiecie że istnieje coś takiego jak unicode?");
      Console.WriteLine("Lata 90-siąte się skończyły, czemu nawet kodowania nie podacie?");
      Console.WriteLine("I muszę teraz to na unicode konwertować");
      var slownik = File.ReadAllLines("slownik.txt");
      var wordList = new List<string>(slownik);
      foreach (string str in wordList) {
        Console.WriteLine(str.replace("¿", ""));
      }
    }
  }
}
