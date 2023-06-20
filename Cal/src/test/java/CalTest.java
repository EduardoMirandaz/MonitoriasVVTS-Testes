
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class CalTest {
	
	static Cal c1;

	@BeforeAll
	static void setUpBeforeClass() throws Exception {
		c1 = new Cal();
	}

	@AfterAll
	static void tearDownAfterClass() throws Exception {
		c1 = null;
	}
	
	@BeforeEach
	void setUp() throws Exception {
	}

	@AfterEach
	public void tearDown() {
	}
	
	@Test
	// sem argumentos
    public void teste0() {
		Assertions.assertDoesNotThrow(() -> Cal.main(new String[] {}));
	}
	
	@Test
	// anos invalidos
    public void teste1() {
		Assertions.assertDoesNotThrow(() -> Cal.main(new String[] {"", "a"}));
		Assertions.assertDoesNotThrow(() -> Cal.main(new String[] {"10000"}));
		Assertions.assertDoesNotThrow(() -> Cal.main(new String[] {"1", "10000"}));
	}
	
	@Test
	//meses invalidos 
	public void teste2() {
		Assertions.assertDoesNotThrow(() -> Cal.main(new String[] {"a"}));
		Assertions.assertDoesNotThrow(() -> Cal.main(new String[] {"13"}));
		Assertions.assertDoesNotThrow(() -> Cal.main(new String[] {"1", "a"}));
		Assertions.assertDoesNotThrow(() -> Cal.main(new String[] {"0", "2022"}));
		Assertions.assertDoesNotThrow(() -> Cal.main(new String[] {"13", "2022"}));
	}
	
	@Test
	// mes e ano validos
    public void teste3() {
		Assertions.assertDoesNotThrow(() -> Cal.main(new String[] {"1", "2023"}));
	}
	
	@Test
	//metodo numberOfDays
	void teste4() {
        Assertions.assertEquals(19, c1.numberOfDays(9, 1752));
        // mes =! 2 || 9 && ano 1752
        Assertions.assertEquals(31, c1.numberOfDays(1, 1752));
		// mes = 2 && ano bissexto
        Assertions.assertEquals(29, c1.numberOfDays(2, 2020));
        // mes > 2 && ano bissexto
        Assertions.assertEquals(31, c1.numberOfDays(3, 2020));
		// mes =! 2 || 9 && ano nao bissexto
		Assertions.assertEquals(31, c1.numberOfDays(1, 2023));
	}
	
	@Test
	//metodo firstOfMonth
    public void teste5() {
        // mes < 2 && ano 1752
        Assertions.assertEquals(3, c1.firstOfMonth(1, 1752));
		// mes > 9 && ano 1752
        Assertions.assertEquals(0, c1.firstOfMonth(10, 1752));
        // mes > 2 && ano bissexto
        Assertions.assertEquals(0, c1.firstOfMonth(3, 2020));
        // mes < 2 && ano nao bissexto
        Assertions.assertEquals(0, c1.firstOfMonth(1, 2023));
    }
	
	@Test
	//metodo isLeap
	void teste6() {
        // ano <= 1752 && nao bissexto
        Assertions.assertEquals(false, c1.isLeap(1751));
		// ano <= 1752 && bissexto
        Assertions.assertEquals(true, c1.isLeap(1752));
        // ano % 100 == 0 
        Assertions.assertEquals(false, c1.isLeap(1800));
        // ano % 4 == 0 
        Assertions.assertEquals(true, c1.isLeap(1804));
        // ano % 400 == 0  
        Assertions.assertEquals(true, c1.isLeap(2000));
        // ano nao bissexto
        Assertions.assertEquals(false, c1.isLeap(2023));
	}
	
	@Test
	//metodo cal
	void teste7() {
		// dds = 1 && n != 19
        Assertions.assertEquals("    1  2  3  4  5  6\n"
        		+ " 7  8  9 10 11 12 13\n"
        		+ "14 15 16 17 18 19 20\n", c1.cal(1, 20));
		// dds = 1 && n = 19
        Assertions.assertEquals("       1  2 14 15 16\n"
        		+ "17 18 19 20 21 22 23\n"
        		+ "24 25 26 27 28 29 30", c1.cal(1, 19));
	}
}