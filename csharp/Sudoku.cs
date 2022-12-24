using System;
using System.Collections.Generic;

namespace Sudoku
{
    class Point
    {
        public int i { get; set; }
        public int j { get; set; }

        public Point(int i, int j)
        {
            this.i = i;
            this.j = j;
        }
    }
    class Sudoku
    {
        public static void display(int[,] data)
        {
            for (int i = 0; i < 9; i++)
            {
                for (int j = 0; j < 9; j++)
                {
                    Console.Write(data[i, j]);
                    Console.Write(" ");
                }
                Console.WriteLine("");
            }
        }
        public static bool isInsideRow(int[,] data, int row,  int num)
        {
            for (int j = 0; j < 9; j++)
            {
                if (data[row, j] == num) return true;
            }
            return false;
        }
        public static bool isInsideColumn(int[,] data, int col, int num)
        {
            for (int i = 0; i < 9; i++)
            {
                if (data[i, col] == num) return true;
            }
            return false;
        }
        public static bool isInsideBox(int[,] data, int row, int col, int num)
        {
            int rowStart = row - row % 3;
            int colStart = col - col % 3;
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (data[rowStart + i, colStart + j] == num)
                    {
                        return true;
                    }
                }
            }
            return false;
        }
        public static bool canFill(int[,] data, int row, int col, int num)
        {
            return data[row, col] == 0 && !isInsideRow(data, row, num) && !isInsideColumn(data, col, num) && !isInsideBox(data, row, col, num);
        }
        public static List<Point> findEmptyPos(int[,] data)
        {
            List<Point> lst = new List<Point>();
            for (int i = 0; i < 9; i++)
            {
                for (int j = 0; j < 9; j++)
                {
                    if (data[i,j] == 0)
                    {
                        lst.Add(new Point(i, j));
                    }
                }
            }
            return lst;
        }

        public static bool solve(int[,] data, List<Point> emptySpaces, int head= 0)
        {
            if (head >= emptySpaces.Count) return true;
            Point p = emptySpaces[head];
            int i = p.i;
            int j = p.j;

            for (int num = 1; num<= 9; num++){
                if (canFill(data, i, j, num))
                {
                    data[i, j] = num;
                    if(solve(data, emptySpaces, head+1)) return true;
                    data[i, j] = 0;
                }
            }
            return false;
        }

        static void Main(string[] args)
        {
            int[,] data = new int[9, 9]{
                      {8, 0, 0, 0, 0, 0, 0, 0, 0},
                      {0, 0, 3, 6, 0, 0, 0, 0, 0},
                      {0, 7, 0, 0, 9, 0, 2, 0, 0},
                      {0, 5, 0, 0, 0, 7, 0, 0, 0},
                      {0, 0, 0, 0, 4, 5, 7, 0, 0},
                      {0, 0, 0, 1, 0, 0, 0, 3, 0},
                      {0, 0, 1, 0, 0, 0, 0, 6, 8},
                      {0, 0, 8, 5, 0, 0, 0, 1, 0},
                      {0, 9, 0, 0, 0, 0, 4, 0, 0}};

            List<Point> emptySpaces = findEmptyPos(data);
            if(solve(data, emptySpaces))
            {
                display(data);
            }
            else
            {
                Console.WriteLine("No solution!!");
            }
            

            Console.ReadKey();
        }
    }
}
