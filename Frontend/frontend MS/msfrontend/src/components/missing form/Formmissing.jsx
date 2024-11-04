import React, { useState } from "react";
import "./formmissing.css";
import axios from "axios";
import formimage from "../../images/form.gif";

const Formmissing = () => {
  const [user, setUser] = useState({
    name: "",
    email: "",
    datemissing: "",
    identification: "",
    adhaar_number: "",
    address: "",
    height: 0,
    phonenumber: "",
    Gender: "",
  });
  const [image, setImage] = useState(null);

  // Handle form input changes
  const handleInput = (e) => {
    const { name, value, type, files } = e.target;

    if (type === "file") {
      setImage(files[0]);
    } else {
      setUser({ ...user, [name]: value });
    }
  };

  // Handle form submission
  const postdata = async (e) => {
    e.preventDefault();
    const formData = new FormData();

    // Append all properties of the `user` object to the form
    Object.keys(user).forEach((key) => {
      formData.append(key, user[key]);
    });

    if (image) {
      formData.append("image", image);
    }

    try {
      const res = await axios.post(
        "http://localhost:3000/api/missingpeople/addperson",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      if (res.status === 200) {
        window.alert("Registration successful");
      } else {
        window.alert("Invalid registration");
      }
    } catch (error) {
      console.error("Error in registration:", error);
      window.alert("Error occurred during registration");
    }
  };

  return (
    <div className="fullformpage">
      <div className="formout">
        <div className="containerform">
          <div className="title">Registration</div>
          <div className="content">
            <form method="POST" onSubmit={postdata}>
              <div className="user-details">
                <div className="input-box">
                  <span className="details">Full Name</span>
                  <input
                    type="text"
                    placeholder="Enter person's name"
                    name="name"
                    value={user.name}
                    onChange={handleInput}
                    required
                  />
                </div>
                <div className="input-box">
                  <span className="details">Email</span>
                  <input
                    type="email"
                    placeholder="Enter your email"
                    name="email"
                    value={user.email}
                    onChange={handleInput}
                    required
                  />
                </div>
                <div className="input-box">
                  <span className="details">Date Missing</span>
                  <input
                    type="date"
                    name="datemissing"
                    value={user.datemissing}
                    onChange={handleInput}
                    required
                  />
                </div>
                <div className="input-box">
                  <span className="details">Identification</span>
                  <input
                    type="text"
                    placeholder="Enter identification mark"
                    name="identification"
                    value={user.identification}
                    onChange={handleInput}
                    required
                  />
                </div>
                <div className="input-box">
                  <span className="details">Aadhaar Number</span>
                  <input
                    type="text"
                    placeholder="Enter Aadhaar number"
                    name="adhaar_number"
                    value={user.adhaar_number}
                    onChange={handleInput}
                    required
                  />
                </div>
                <div className="input-box">
                  <span className="details">Address</span>
                  <input
                    type="text"
                    placeholder="Enter address"
                    name="address"
                    value={user.address}
                    onChange={handleInput}
                    required
                  />
                </div>
                <div className="input-box">
                  <span className="details">Height</span>
                  <input
                    type="number"
                    placeholder="Enter height (in feet)"
                    name="height"
                    value={user.height}
                    onChange={handleInput}
                    required
                  />
                </div>
                <div className="input-box">
                  <span className="details">Phone Number</span>
                  <input
                    type="tel"
                    placeholder="Enter contact number"
                    name="phonenumber"
                    value={user.phonenumber}
                    onChange={handleInput}
                    required
                  />
                </div>
                <div className="input-box">
                  <span className="details">Person Image</span>
                  <input
                    type="file"
                    name="image"
                    accept="image/*"
                    onChange={handleInput}
                    required
                  />
                </div>
              </div>

              <div className="gender-details">
                <input
                  type="radio"
                  name="Gender"
                  id="dot-1"
                  value="male"
                  onChange={handleInput}
                />
                <input
                  type="radio"
                  name="Gender"
                  id="dot-2"
                  value="female"
                  onChange={handleInput}
                />
                <input
                  type="radio"
                  name="Gender"
                  id="dot-3"
                  value="others"
                  onChange={handleInput}
                />
                <span className="gender-title">Gender</span>
                <div className="category">
                  <label htmlFor="dot-1">
                    <span className="dot one"></span>
                    <span className="gender">Male</span>
                  </label>
                  <label htmlFor="dot-2">
                    <span className="dot two"></span>
                    <span className="gender">Female</span>
                  </label>
                  <label htmlFor="dot-3">
                    <span className="dot three"></span>
                    <span className="gender">Others</span>
                  </label>
                </div>
              </div>
              <div className="button">
                <input type="submit" value="Register" />
              </div>
            </form>
          </div>
        </div>
      </div>

      <div className="photoform">
        <div className="textphoto">
          Get the missing person Registered with us and get them found with our
          face recognition methods.
        </div>
        <img src={formimage} alt="Form GIF" width="400px" />
      </div>
    </div>
  );
};

export default Formmissing;
