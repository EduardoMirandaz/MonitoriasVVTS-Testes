/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author grazi
 */
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalTest {
    public void testFirstOfMonth() {
        Cal cal = new Cal();
        
        // Teste com mês válido e ano válido
        int dayOfWeek1 = cal.firstOfMonth(2, 2023);
        assertEquals(1, cal.firstOfMonth(2, 2023));
        
        // Teste com mês inválido
        int dayOfWeek2 = cal.firstOfMonth(0, 2023);
        assertEquals(-1, dayOfWeek2);
        
        // Teste com ano inválido
        int dayOfWeek3 = cal.firstOfMonth(2, 10000);
        assertEquals(-1, dayOfWeek3);
    }

    public void testNumberOfDays() {
        Cal cal = new Cal();
        
        // Teste com mês válido e ano válido
        int numberOfDays1 = cal.numberOfDays(2, 2023);
        assertEquals(28, numberOfDays1);
        
        // Teste com mês inválido
        int numberOfDays2 = cal.numberOfDays(0, 2023);
        assertEquals(-1, numberOfDays2);
        
        // Teste com ano inválido
        int numberOfDays3 = cal.numberOfDays(2, 10000);
        assertEquals(-1, numberOfDays3);
    }

    public void testIsLeap() {
        Cal cal = new Cal();
        
        // Teste com ano bissexto
        boolean isLeap1 = cal.isLeap(2020);
        assertTrue(isLeap1);
        
        // Teste com ano não bissexto
        boolean isLeap2 = cal.isLeap(2023);
        assertFalse(isLeap2);
    }

    public void testCal() {
        Cal cal = new Cal();
        
        // Teste com valores válidos
        String expectedCalendar1 = "   1  2  3  4  5  6  7\n" +
                                   " 8  9 10 11 12 13 14\n" +
                                   "15 16 17 18 19 20 21\n" +
                                   "22 23 24 25 26 27 28";
        String calendar1 = cal.cal(1, 28);
        assertEquals(expectedCalendar1, calendar1);
        
        // Teste com número de dias inválido
        String expectedCalendar2 = "";
        String calendar2 = cal.cal(1, 0);
        assertEquals(expectedCalendar2, calendar2);
    }

    public void testJan1() {
        Cal cal = new Cal();
        
        // Teste com ano válido
        int dayOfWeek1 = cal.jan1(2023);
        assertEquals(1, dayOfWeek1);
        
        // Teste com ano inválido
        int dayOfWeek2 = cal.jan1(10000);
        assertEquals(-1, dayOfWeek2);
    }
}

