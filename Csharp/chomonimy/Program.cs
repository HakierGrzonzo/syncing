// Zadanie 4, chomonimy, C#
// Plik slownik.txt powinien być w katalogu w którym jest program
// Program tworzy nowe wątki
﻿using System;
using System.Collections.Generic;


namespace chomonimy
{
  class Node
  {
    public string letter;
    public List<Node> children = new List<Node>();
    public Node(string letter)
    {
      this.letter = letter;
    }
    public static void add(string word)
    {
      if (this.letter != word) {
        foreach (Node child in this.children) {
          if (child.letter == word[0]) {
            child.add(word.Substring(1));
            break;
          }
        }
      }
    }
    public static bool isIn(string word)
    {
      if (word == this.letter){
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
      Console.WriteLine("Hello World!");
    }
  }
}
