using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace problem102
{
    class Program
    {
        public static bool ContainsOrigin(int ax, int ay, int bx, int by, int cx, int cy)
        {
            if (On0(ax, ay, bx, by, cx, cy))
                return true;
            if (Between0(ax, bx, cx))
        }
        public static double Incline(double ax, double ay, double bx, double by)
        {
            return (ay - by) / (ax - bx);
        }
        public static double Coefficient(double ax, double ay, double bx, double by)
        {
            return ay - ax * Incline(ax, ay, bx, by);
        }
        public static bool On0(double ax, double ay, double bx, double by, double cx, double cy)
        {
            return (ax == 0 && ay == 0) || (bx == 0 && by == 0) || (cx == 0 && cy == 0);
        }
        public static bool Between0(double ax, double bx, double cx)
        {
            return (ax > 0 != bx > 0) && (ax > 0 != cx > 0);
        }
        static void Main(string[] args)
        {
            Console.WriteLine("for the points a = (-340, 495), b = (-153, -910), the equation of the line is:");
            Console.WriteLine("y = " + Incline(-340, 495, -153, -910) + "* x + " + Coefficient(-340, 495, -153, -910));
            Console.ReadKey();
        }
    }
}
