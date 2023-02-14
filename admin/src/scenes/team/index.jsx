/** @format */

import { Box, Typography, useTheme } from "@mui/material";
import { useEffect, useState } from "react";
import { DataGrid } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import AdminPanelSettingsOutlinedIcon from "@mui/icons-material/AdminPanelSettingsOutlined";
import LockOpenOutlinedIcon from "@mui/icons-material/LockOpenOutlined";
import SecurityOutlinedIcon from "@mui/icons-material/SecurityOutlined";
import Header from "../../components/Header";

const Team = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [columns, setColumns] = useState([
    { field: "id", headerName: "ID" },
    { field: "first_name", headerName: "First Name" },
    { field: "last_name", headerName: "Last Name" },
    { field: "guardian", headerName: "Guardian" },
    { field: "gender", headerName: "Gender" },
    { field: "dob", headerName: "Date of Birth" },
    { field: "street1", headerName: "Street 1" },
    { field: "street2", headerName: "Street 2" },
    { field: "city", headerName: "City" },
    { field: "state", headerName: "State" },
    { field: "country", headerName: "Country" },
    { field: "zip", headerName: "ZIP" },
    { field: "phone", headerName: "Phone" },
    { field: "email", headerName: "Email" },
    { field: "language_preference", headerName: "Language Preference" },
    { field: "species", headerName: "Species" },
    {
      field: "viewed_notice_of_privacy_practices",
      headerName: "Viewed Notice of Privacy Practices",
    },
    {
      field: "viewed_notice_of_privacy_practices_date",
      headerName: "Date Notice of Privacy Practices Viewed",
    },
  ]);

  const [rows, setRows] = useState([]);

  useEffect(() => {
    async function getData() {
      const request = fetch("http://localhost:8000/patients");
      const response = await request;
      const parsed = await response.json();
      setRows(parsed);
    }
    getData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  console.log(rows);

  //   console.log("Columns:", columns);
  //   console.log("Rows:", rows);

  return (
    <Box m="20px">
      <Header title="Patient View" subtitle="Managing the Patients" />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
        }}>
        <DataGrid rows={rows} columns={columns} />
      </Box>
    </Box>
  );
};

export default Team;
