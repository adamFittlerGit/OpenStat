import { Inter } from "next/font/google";
import dynamic from "next/dynamic";
import "./globals.css";
import SearchAppBar from "@/components/Appbar";

const inter = Inter({ subsets: ["latin"] });

const metadata = {
  title: "Openstatistics",
  description: "Providing statistics visualisations for openpowerlifting data!",
};

export default function RootLayout({ children }) {
  return (
    <>
      <html>
        <head>
          <title>{metadata.title}</title>
          <meta name="description" content={metadata.description} />
          {/* Add any other necessary meta tags, links, or scripts */}
        </head>
        <body>
          <SearchAppBar/>
          <div className={inter.className}>
            {/* Include your content inside the body tag */}
            {children}
          </div>
        </body>
      </html>
    </>
  );
}
