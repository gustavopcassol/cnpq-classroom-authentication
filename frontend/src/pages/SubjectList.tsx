import "./SubjectList.css";
import { useEffect, useState } from "react";
import ListGroup from "react-bootstrap/ListGroup";
import Container from "react-bootstrap/Container";
import ConfirmationModal from "../components/ConfirmationModal";
import { attendLecture, loadLectures } from "../external/backend";

interface Lecture {
  id: number;
  course: string;
  is_ongoing: boolean;
  has_attended: boolean;
}

export default function SubjectList(): JSX.Element {
  const [showConfirmation, setShowConfirmation] = useState(false);
  const [lectures, setLectures] = useState<readonly Lecture[]>([]);
  const [selectedLectureId, setSelectedLectureId] = useState(0);

  useEffect(() => {
    loadAndSetLectures();
  }, []);

  const loadAndSetLectures = async () => {
    const response = await loadLectures();
    setLectures(await response.json());
  };

  const handleConfirmationAccept = async () => {
    setShowConfirmation(false);
    await attendLecture(selectedLectureId);
    await loadAndSetLectures();
  };

  const getListGroupProps = (lecture: Lecture) => {
    if (lecture.has_attended) {
      return {
        variant: "success",
      };
    }
    if (lecture.is_ongoing) {
      return {
        action: true,
        onClick: () => handleListGroupItemClick(lecture.id),
        active: true,
      };
    }
    return {};
  };

  const handleListGroupItemClick = (lectureId: number) => {
    setShowConfirmation(true);
    setSelectedLectureId(lectureId);
  };

  const listGroupItems = lectures.map((v, i) => (
    <ListGroup.Item
      className="list-group__item"
      key={i}
      {...getListGroupProps(v)}
    >
      {v.course}
    </ListGroup.Item>
  ));

  return (
    <>
      <ConfirmationModal
        show={showConfirmation}
        handleClose={() => setShowConfirmation(false)}
        handleAccept={handleConfirmationAccept}
      />
      <Container className="container">
        <h1 className="title-heading">registro de presença</h1>
        {lectures.length === 0 ? (
          <h5 className="list-heading text-muted">
            não há aulas para registrar presença.
          </h5>
        ) : (
          <>
            <h5 className="list-heading text-muted">
              selecione aula para registrar presença.
            </h5>
            <ListGroup className="list-group">{listGroupItems}</ListGroup>
          </>
        )}
      </Container>
    </>
  );
}
