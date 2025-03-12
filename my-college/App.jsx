import { useState } from "react";

export default function CollegeApp() {
  const [theme, setTheme] = useState("dark");

  const toggleTheme = () => {
    setTheme(theme === "dark" ? "light" : "dark");
  };

  return (
    <div className={theme === "dark" ? "bg-gray-900 text-white" : "bg-white text-black"}>
      {/* Header */}
      <header className="relative h-80 bg-cover bg-center bg-[url('/college.jpg')] brightness-75">
        <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
          <h1 className="text-3xl font-bold">Добро пожаловать в наш колледж</h1>
          <p className="mt-2">Качественное образование для успешного будущего</p>
          <button
            className="mt-4 px-6 py-2 bg-blue-600 text-white rounded-lg shadow-lg hover:bg-blue-800"
            onClick={() => window.location.href = '/about'}
          >Подробнее о нас</button>
        </div>
      </header>
      
      {/* Telegram Widget */}
      <div className="flex justify-center py-4">
        <script async src="https://telegram.org/js/telegram-widget.js?7"
                data-telegram-login="MAGICCAYPbot"
                data-size="large"
                data-auth-url="https://your-server.com/auth"
                data-request-access="write">
        </script>
      </div>

      {/* Main Content */}
      <main className="container mx-auto p-4">
        <section className="bg-gray-800 p-4 rounded-lg shadow-lg border border-blue-500">
          <h2 className="text-xl font-bold">📰 Новости</h2>
          <div className="mt-2">
            <p className="font-semibold">День открытых дверей</p>
            <p className="text-sm text-gray-400">15 марта 2024</p>
            <p>Приглашаем всех желающих познакомиться с нашим колледжем.</p>
          </div>
          <div className="mt-2">
            <p className="font-semibold">Победа в городской олимпиаде</p>
            <p className="text-sm text-gray-400">10 марта 2024</p>
            <p>Наши студенты заняли первое место в городской олимпиаде по программированию.</p>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="fixed bottom-0 w-full bg-gray-800 py-3 flex justify-around border-t border-gray-700">
        <button className="px-4 py-2 bg-gray-600 text-white rounded-lg" onClick={() => window.location.href = '/'}>🏠 Главная</button>
        <button className="px-4 py-2 bg-gray-600 text-white rounded-lg" onClick={() => window.location.href = '/materials'}>📚 Методички</button>
        <button className="px-4 py-2 bg-gray-600 text-white rounded-lg" onClick={() => window.location.href = '/schedule'}>🗓️ Расписание</button>
        <button className="px-4 py-2 bg-gray-600 text-white rounded-lg" onClick={toggleTheme}>Сменить тему</button>
      </footer>
    </div>
  );
}
