import { Link, NavLink } from "react-router-dom";

const navLinks = [
  { title: "Tools", link: "/tools" },
  { title: "Blog", link: "/blog" },
  { title: "Contact", link: "/contact" },
  { title: "About", link: "/about" },
];

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-slate-200 bg-white">
      <nav className="mx-auto flex h-16 w-full max-w-7xl items-center justify-between px-20">
        <Link to="/" className="flex items-center gap-3">
          <img
            src="https://res.cloudinary.com/dyvkdwzcj/image/upload/v1709055594/logo-1_vo1dni.png"
            className="h-8 w-8 rounded"
            alt="Logo"
          />
          <span className="self-center whitespace-nowrap text-xl font-semibold text-stone-900 md:text-2xl">
            Project
          </span>
        </Link>

        <div className="flex items-center gap-2 sm:gap-3">
          {navLinks.map((item) => (
            <NavLink
              key={item.title}
              to={item.link}
              className={({ isActive }) =>
                [
                  "rounded-md px-3 py-2 text-sm font-medium transition",
                  isActive
                    ? "bg-slate-900 text-white"
                    : "text-slate-600 hover:bg-slate-100 hover:text-slate-900",
                ].join(" ")
              }
            >
              {item.title}
            </NavLink>
          ))}
        </div>
      </nav>
    </header>
  );
}
