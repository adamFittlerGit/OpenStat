import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import SearchAppBar from '../components/Appbar';

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Openstatistics",
  description: "Providing statistics visualisations for openpowerlifting data!",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <>
      <SearchAppBar />
      <div className={inter.className}>{children}</div>
    </>
  );
}
