// JavaScript to handle popup display and close

//Post 

// update vdo user 

// search box
document.getElementById('searchInput').addEventListener('input', function() {
    const searchValue = this.value.toLowerCase();
    const usersResult = document.getElementById('usersResult');
  
    // Make an AJAX request to fetch usernames based on search input
    fetch(`/get_usernames/?search=${searchValue}`)
        .then(response => response.json())
        .then(data => {
            usersResult.innerHTML = '';
            data.forEach(username => {
                const li = document.createElement('li');
                li.textContent = username;
                usersResult.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching usernames:', error));
  
    // Show the popup
    document.getElementById('searchResults').style.display = 'block';
});

function closePopup() {
    document.getElementById('searchResults').style.display = 'none';
}

/*
document.getElementById('searchInput').addEventListener('input', function() {
  const searchValue = this.value.toLowerCase();
  const usersResult = document.getElementById('usersResult');

  // Simulating fetching users from a database (replace with your data fetching logic)
 
  const usersFromDatabase = [
   
    'John Doe',
    'Jane Smith',
    'Alice Johnson',
    'Bob Brown',
    'Eva Green',
    'Sam Wilson'
    // Add more users or fetch from a real database
  ];
  
  // Filter users based on the search value
  const filteredUsers = usersFromDatabase.filter(user =>
    user.toLowerCase().includes(searchValue)
  );

  // Clear previous search results
  usersResult.innerHTML = '';

  // Display filtered users in the popup
  filteredUsers.forEach(user => {
    const li = document.createElement('li');
    li.textContent = user;
    usersResult.appendChild(li);
  });

  // Show the popup
  document.getElementById('searchResults').style.display = 'block';
});

// Function to close the popup
function closePopup() {
  document.getElementById('searchResults').style.display = 'none';
}

*/

// post Area

document.getElementById('postButton').addEventListener('click', submitPost);

function submitPost() {
  var postText = document.getElementById('postTextArea').value;
  var videoFile = document.getElementById('videoInput').files[0];
  var photoFile = document.getElementById('photoInput').files[0];

  if (videoFile && !photoFile) {
    // Post with video
    var uniqueId = generateUniqueId();
    console.log('Post Text with Video:', postText);
    console.log('Video File:', videoFile);
    console.log('Unique ID:', uniqueId);
  } else if (photoFile && !videoFile) {
    // Post with photo
    var uniqueId = generateUniqueId();
    console.log('Post Text with Photo:', postText);
    console.log('Photo File:', photoFile);
    console.log('Unique ID:', uniqueId);
  } else if (!videoFile && !photoFile) {
    // Post with only text
    var uniqueId = generateUniqueId();
    console.log('Post Text Only:', postText);
    console.log('Unique ID:', uniqueId);
  } else {
    // Error: Both video and photo uploaded
    console.error('Please upload either a video or an image, not both.');
  }

  // Clear input fields if needed
  document.getElementById('postTextArea').value = '';
  document.getElementById('videoInput').value = '';
  document.getElementById('photoInput').value = '';
}

function generateUniqueId() {
  return Math.floor(Math.random() * 1000000);
}


// post 5

let likeCountFive = 0; // Initial like count for post 5
let commentCountFive = 0; // Initial comment count for post 5

function likePostFive() {
    likeCountFive++; // Increment the like count for post 5
    document.getElementById('likeCountFive').textContent = likeCountFive;
}

function showCommentPopupFive() {
    document.getElementById('commentPopupFive').style.display = 'block';
}

function closeCommentPopupFive() {
    document.getElementById('commentPopupFive').style.display = 'none';
}

function addCommentFive() {
    const comment = document.getElementById('commentInputFive').value;
    // Perform actions with the comment, e.g., display it
    console.log('Added comment for post 5:', comment);
    commentCountFive++; // Increment the comment count for post 5
    document.getElementById('commentCountFive').textContent = commentCountFive;
    closeCommentPopupFive(); // Close the comment popup for post 5 after adding a comment
}


// post 4

let likeCountFour = 0; // Initial like count for post 4
let commentCountFour = 0; // Initial comment count for post 4

function likePostFour() {
    likeCountFour++; // Increment the like count for post 4
    document.getElementById('likeCountFour').textContent = likeCountFour;
}

function showCommentPopupFour() {
    document.getElementById('commentPopupFour').style.display = 'block';
}

function closeCommentPopupFour() {
    document.getElementById('commentPopupFour').style.display = 'none';
}

function addCommentFour() {
    const comment = document.getElementById('commentInputFour').value;
    // Perform actions with the comment, e.g., display it
    console.log('Added comment for post 4:', comment);
    commentCountFour++; // Increment the comment count for post 4
    document.getElementById('commentCountFour').textContent = commentCountFour;
    closeCommentPopupFour(); // Close the comment popup for post 4 after adding a comment
}


//post3

let likeCountTwo = 0; // Initial like count for post 2
let commentCountTwo = 0; // Initial comment count for post 2

function likePostTwo() {
    likeCountTwo++; // Increment the like count for post 2
    document.getElementById('likeCountTwo').textContent = likeCountTwo;
}

function showCommentPopupTwo() {
    document.getElementById('commentPopupTwo').style.display = 'block';
}

function closeCommentPopupTwo() {
    document.getElementById('commentPopupTwo').style.display = 'none';
}

function addCommentTwo() {
    const comment = document.getElementById('commentInputTwo').value;
    // Perform actions with the comment, e.g., display it
    console.log('Added comment for post 2:', comment);
    commentCountTwo++; // Increment the comment count for post 2
    document.getElementById('commentCountTwo').textContent = commentCountTwo;
    closeCommentPopupTwo(); // Close the comment popup for post 2 after adding a comment
}

// post2
let likeCount2 = 0; // Initial like count
let commentCount2 = 0; // Initial comment count

function likePost2() {
    likeCount2++; // Increment the like count
    document.getElementById('likeCount2').textContent = likeCount2;
}

function showCommentPopup2() {
    document.getElementById('commentPopup2').style.display = 'block';
}

function closeCommentPopup2() {
    document.getElementById('commentPopup2').style.display = 'none';
}

function addComment2() {
    const comment = document.getElementById('commentInput2').value;
    // Perform actions with the comment, e.g., display it
    console.log('Added comment:', comment);
    commentCount2++; // Increment the comment count
    document.getElementById('commentCount2').textContent = commentCount2;
    closeCommentPopup2(); // Close the comment popup after adding a comment
}


// For post 1



let likeCount = 0; // Initial like count
let commentCount =0; // Initial comment count

function likePost() {
    likeCount++; // Increment the like count
    document.getElementById('likeCount').textContent = likeCount;
}

function showCommentPopup() {
    document.getElementById('commentPopup').style.display = 'block';
}

function closeCommentPopup() {
    document.getElementById('commentPopup').style.display = 'none';
}

function addComment() {
    const comment = document.getElementById('commentInput').value;
    // Perform actions with the comment, e.g., display it
    console.log('Added comment:', comment);
    commentCount++; // Increment the comment count
    document.getElementById('commentCount').textContent = commentCount;
    closeCommentPopup(); // Close the comment popup after adding a comment
}



// Story player

document.querySelector('.story.story5').addEventListener('click', function() {
    const videoPlayer = document.querySelector('.videoPlayer');
    videoPlayer.style.display = 'block';
  
    const video = document.getElementById('myVideo');
    const playButton = document.getElementById('playButton');
    const closeButton = document.getElementById('closeButton');
  
    playButton.addEventListener('click', function() {
        if (video.paused) {
            video.play();
            playButton.textContent = 'Pause';
        } else {
            video.pause();
            playButton.textContent = 'Play';
        }
    });
  
    closeButton.addEventListener('click', function() {
        videoPlayer.style.display = 'none';
        video.pause();
        video.src = '';
        playButton.textContent = 'Play';
    });
    
  });
  
document.querySelector('.story.story4').addEventListener('click', function() {
  const videoPlayer = document.querySelector('.videoPlayer');
  videoPlayer.style.display = 'block';

  const video = document.getElementById('myVideo');
  const playButton = document.getElementById('playButton');
  const closeButton = document.getElementById('closeButton');

  playButton.addEventListener('click', function() {
      if (video.paused) {
          video.play();
          playButton.textContent = 'Pause';
      } else {
          video.pause();
          playButton.textContent = 'Play';
      }
  });

  closeButton.addEventListener('click', function() {
      videoPlayer.style.display = 'none';
      video.pause();
      video.src = '';
      playButton.textContent = 'Play';
  });
});

document.querySelector('.story.story3').addEventListener('click', function() {
  const videoPlayer = document.querySelector('.videoPlayer');
  videoPlayer.style.display = 'block';

  const video = document.getElementById('myVideo');
  const playButton = document.getElementById('playButton');
  const closeButton = document.getElementById('closeButton');

  playButton.addEventListener('click', function() {
      if (video.paused) {
          video.play();
          playButton.textContent = 'Pause';
      } else {
          video.pause();
          playButton.textContent = 'Play';
      }
  });

  closeButton.addEventListener('click', function() {
      videoPlayer.style.display = 'none';
      video.pause();
      video.src = '';
      playButton.textContent = 'Play';
  });
});

document.querySelector('.story.story2').addEventListener('click', function() {
  const videoPlayer = document.querySelector('.videoPlayer');
  videoPlayer.style.display = 'block';

  const video = document.getElementById('myVideo');
  const playButton = document.getElementById('playButton');
  const closeButton = document.getElementById('closeButton');

  playButton.addEventListener('click', function() {
      if (video.paused) {
          video.play();
          playButton.textContent = 'Pause';
      } else {
          video.pause();
          playButton.textContent = 'Play';
      }
  });

  closeButton.addEventListener('click', function() {
      videoPlayer.style.display = 'none';
      video.pause();
      video.src = '';
      playButton.textContent = 'Play';
  });
});


document.querySelector('.story.story1').addEventListener('click', function() {
  const videoPlayer = document.querySelector('.videoPlayer');
  videoPlayer.style.display = 'block';

  const video = document.getElementById('myVideo');
  const playButton = document.getElementById('playButton');
  const closeButton = document.getElementById('closeButton');

  playButton.addEventListener('click', function() {
      if (video.paused) {
          video.play();
          playButton.textContent = 'Pause';
      } else {
          video.pause();
          playButton.textContent = 'Play';
      }
  });

  closeButton.addEventListener('click', function() {
      videoPlayer.style.display = 'none';
      video.pause();
      video.src = '';
      playButton.textContent = 'Play';
  });
});


// Player
document.getElementById('uploadImage').addEventListener('click', function() {
  document.getElementById('videoUpload').click();
});

document.getElementById('videoUpload').addEventListener('change', function(e) {
  const file = e.target.files[0];
  const videoPlayer = document.querySelector('.videoPlayer');
  const video = document.getElementById('myVideo');
  const playButton = document.getElementById('playButton');
  const closeButton = document.getElementById('closeButton');

  if (file && file.type.includes('video')) {
      const reader = new FileReader();
      reader.onload = function(event) {
          video.src = event.target.result;
          videoPlayer.style.display = 'block';
      };
      reader.readAsDataURL(file);
  }
  
  playButton.addEventListener('click', function() {
      if (video.paused) {
          video.play();
          playButton.textContent = 'Pause';
      } else {
          video.pause();
          playButton.textContent = 'Play';
      }
  });

  closeButton.addEventListener('click', function() {
      videoPlayer.style.display = 'none';
      video.pause();
      video.src = '';
      playButton.textContent = 'Play';
  });
});




function openPopup(popupId) {
    document.getElementById(popupId).style.display = "block";
  }
  
  function closePopup(popupId) {
    document.getElementById(popupId).style.display = "none";
  }
  
  // JavaScript for handling popup triggers
  document.addEventListener('DOMContentLoaded', function() {
    const popupTriggers = document.querySelectorAll('.popup-trigger');
  
    popupTriggers.forEach(function(trigger) {
      trigger.addEventListener('click', function() {
        const popupId = trigger.textContent.toLowerCase() + '-popup';
        openPopup(popupId);
      });
    });
  });
  